import json

import pandas as pd
from sqlalchemy import create_engine



class Cleaning2:
    def __init__(self):

        self.collumnName = [
            "course_code",
            "type_of_field",
            "course_title",
            "course_title_english",
            "instructor",
            "campus",
            "degree_courses",
            "classtime",
            "type_of_class1",
            "credits(Hrs)",
            "type_of_class2",
            "remarks",
            "type_of_class3"
            ]
        self.df = pd.DataFrame(columns=self.collumnName)
    def datacleaning(self,year):
        with open(rf'data\\01교양\\{year}.json',encoding='UTF8') as f:
            js = json.loads(f.read()) ## json 라이브러리 이용
        df2 = pd.DataFrame(js)
        df2 = pd.read_json(rf'data\\01교양\\{year}.json',encoding='UTF8') ## pd.read_json 이용

        # '담기' 제거
        df2_list = df2['course'].to_list()

        for each in df2_list:
            for i in range(len(each)):
                if each[i] == '담기':
                    idx = i
                    each.remove(each[idx])
                    break

        for each in df2_list:
            for i in range(len(each)):
                if each[i] == '보기':
                    idx = i
                    each.remove(each[idx])
                    break

        # 2021학년도, 2022학년도 일떄
        if year ==  "2020학년도 2학기" or year ==  "2021학년도 1학기" or year == "2021학년도 1학기"or year == "2021학년도 2학기" or year == "2022학년도 1학기" or year == "2022학년도 2학기":
            for each in df2_list:
                if len(each) == 11:
                    each.insert(10,"nan")
                    each.insert(10,"nan")
                if len(each) == 12:
                    each.insert(10,"nan")

        if year == "2020학년도 1학기" or year == "2019학년도 2학기" or year == "2019학년도 1학기":
            for each in df2_list:
                if len(each) == 11:
                    each.insert(10, "nan")
                    each.insert(12, "nan")
                    continue
                if len(each) == 12:
                    each.insert(-2, "nan")

        for i, each in enumerate(df2_list):
            if each[7] == '국제어수업':
                each[7], each[8] = each[8], each[7]

        for each in df2_list:
            if len(each) > 10:
                # 만약 끝에서 두번째 칼럼에 '"문제해결", "혁신수업" 혹은 "국제어"이라는 문자열이 포함되면, 그 전 칼럼과 값 바꿔주기
                if each[-2].find('문제해결') != -1 or each[-2].find('혁신수업') != -1 or each[-2].find('국제어') != -1:
                    # 세번쨰 칼럼에도 위의 글자가 있으면 바꿔주지 않기
                    if each[-3].find('문제해결') != -1 or each[-3].find('혁신수업') != -1 or each[-3].find('국제어') != -1:
                        continue
                    each[-2], each[-3] = each[-3], each[-2]

        for each in df2_list:
            if len(each) > 10:
                # 만약 끝에서 두번째 칼럼에 '"문제해결", "혁신수업" 혹은 "국제어"이라는 문자열이 포함되면, 그 전 칼럼과 값 바꿔주기
                if each[-1].find('온') != -1 or each[-1].find('오프') != -1:
                    # 세번쨰 칼럼에도 위의 글자가 있으면 바꿔주지 않기
                    each.insert(13, "nan")
        for each in df2_list:
            if len(each) > 11:
                i = 0
                while each[-1].find('온') == -1 and each[-1].find('오프') == -1:
                    each.pop()
                    i += 1
                    if i == 3:
                        break

        df2['course'] = df2_list
        for idx in range(13):
            df2[self.collumnName[idx]] = df2['course'].str.get(idx)

        return df2
    def make_df(self, df1):
        for idx, name in  enumerate(self.collumnName):
            df1[name] = df1['course'].str.get(idx)
        df1=df1.drop(['course'], axis='columns')
        self.df = pd.concat([self.df, df1], axis=0)

result = Cleaning2()

season_list = ["2019학년도 1학기", "2019학년도 2학기", "2020학년도 1학기", "2020학년도 2학기", "2021학년도 1학기", "2021학년도 2학기", "2022학년도 1학기", "2022학년도 2학기"]

for season in season_list:
    temp= result.datacleaning(season)
    result.make_df(temp)


engine = create_engine("mysql+pymysql://root:1234@localhost:3306/dsc3037", encoding='utf-8')
conn = engine.connect()
result.df.to_sql(name='liberal arts_subject', con=engine, if_exists='replace', index=False)