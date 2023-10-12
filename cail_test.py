import os
import json
import argparse
import openai
from time import sleep
from collections import Counter
from datetime import datetime
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("--start", default=0, type=int)
parser.add_argument("--end", default=800, type=int)
args = parser.parse_args()

#the openai api
openaikey = ''

#load data
file = open('data/cail2018_sampled.json',encoding='utf-8')
cail_test = []
for line in file.readlines():
    dic = json.loads(line)
    cail_test.append(dic)


def extract_ans(judgment,true_ans):
    judgment = judgment.replace(' ', '')
    ans = judgment.split('\n')
    try:
        ans.remove('')
    except ValueError:
        pass
    print(ans)
    #return ans
    if ans[-1].find('罪和') != -1:
        return ans[-1]
    elif ans[-1].find(true_ans) != -1:
        return true_ans
    else:
        return ans[-1]

baseline = f"""
    案件: {example['fact']}/n
    罪名：
    """
cot = f"""
    案件: {example['fact']}/n
    让我们一步步思考，最后输出被告人构成的罪名：
    """
syllogism = f"""
    在司法三段论中，大前提是具体的法律规范，小前提是案件事实，结论是判决结果。
    案件: {example['fact']}/n
    让我们用司法三段论思考，最后输出被告人构成的罪名：
    """

if __name__ == "__main__":
    now = datetime.now()
    dt_string = now.strftime("%m_%d_%H_%M")
    engine = 'text-davinci-003'
    correct, wrong = 0, 0

    cail_test = cail_test[args.start:args.end]

    filename = f'outputs/cail_sample_{args.start}_e{args.end}_{dt_string}.jsonl'
    print(filename)
    with open(filename,'w') as writer:
    #writer = open(filename, 'w')
        i = 0
        for example in tqdm(cail_test):

            full_prompt = baseline
            i += 1
            key_num = i % 8
            key = openaikey
            # greedy decoding
            got_result = False
            while not got_result:
                try:
                    result = openai.Completion.create(
                        engine=engine,
                        prompt=full_prompt,
                        api_key=key,
                        max_tokens=700, 
                        temperature=0.0,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                    got_result = True
                except Exception:
                    sleep(3)

            judgment = result['choices'][0]['text']
            print(judgment)
            gt_ans = example['meta']['accusation'][0]
            prediction = extract_ans(judgment,gt_ans)
            if prediction == gt_ans:
                correct += 1
            else:
                wrong += 1

            print(prediction,'$',gt_ans, '$', correct / (correct + wrong))

            try:
                tmp = {'fact':example['fact'],'accusation':gt_ans,'prediction':prediction,'original_pre':judgment}
                writer.write(json.dumps(tmp,ensure_ascii=False) + '\n')
            except Exception:
                continue
    writer.close()
    print()
    print(correct / (correct+wrong))

