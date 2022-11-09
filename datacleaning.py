import json

import pandas as pd
from sqlalchemy import create_engine


class Cleaning:
    def __init__(self):
        self.courselist = [
            "온라인 (사전제작)",
            "온라인[사전제작]",
            "온라인 (사전제작+Real Time Streaming)",
            "온라인 (Real Time Streaming)",
            "온-오프혼합 (오프라인 순환출석+Real Time Streaming)",
            "온-오프혼합 (오프라인+Real Time Streaming)",
            "온-오프혼합 (오프라인+강의저장)",
            "온-오프[오프라인+강의저장,Real Time Streaming]",
            "온-오프[오프라인+강의저장]",
            "온-오프[오프라인+Real Time Streaming]",
            "오프라인",
            "오프라인 (일부 주차 오프라인+잔여 주차 Real Time Streaming)",
            "오프라인 (일부 주차 오프라인+잔여 주차 사전제작영상)",
            "온-오프혼합 (오프라인 순환출석+강의저장)",
            "글로벌-혁신[온라인사전강의 + 오프라인 또는 온라인 Real Time Streaming",
            "nan",
        ]
        self.collumnName = [
            "degree_courses",
            "type_of_field3",
            "course_code",
            "course_title",
            "course_title_english",
            "instructor",
            "campus",
            "type_of_field2",
            "credits(Hrs)",
            "classtime",
            "type_of_class1",
            "type_of_class2",
            "remarks",
        ]
        self.df = pd.DataFrame(columns=self.collumnName)
    def open_json(self, major, season):
        with open(rf"data\\{major}\\{season}.json", encoding="UTF8") as f:
            js = json.load(f)
        df1 = pd.DataFrame(js)
        df1 = pd.read_json(rf"data\\{major}\\{season}.json", encoding="UTF8")
        return df1

    def cleaning(self, df1):
        df2_list = df1['course'].to_list()
        
        # 보기 삭제
        for each in df2_list:
            for i in range(len(each)):
                if each[i]== '보기':
                    idx = i
                    each.remove(each[idx])
                    break
        # 영역구분 3 만들어 주기
        for each in df2_list:
            if each[1] == "전공코어" or each[1] == "전공심화" or each[1] == "실험실습":
                continue
            else:
                each.insert(1, "nan")

        # 교수님 이름 없을때
        for each in df2_list:
            if each[5] == "인문사회" or each[5] == "자연과학":
                each.insert(5, "nan")

        # 수업방식2
        for each in df2_list:
            if len(each) == 11:
                each.append("nan")

        # 13번째 collumn은 비고 칸
        for each in df2_list:
            if len(each) == 12:
                each.append("nan")

        for each in df2_list:
            count = 0
            for class_way in  self.courselist:
                if each[-2] == class_way:
                    count = 1
            if count == 0:
                temp = each[-2]
                each[-1] = temp    
                each[-2] = 'nan'  

        # remove_list = []
        # for idx, each in enumerate(iterable = df2_list):
        #     if len(each)<=6:
        #         remove_list.append(idx)
        # for idx in remove_list:
        #     df2_list.pop(idx)
        #     df1['course'].drop(idx)
                
        df1['course'] = df2_list
        return df1
    
    def make_df(self, df1):
        for idx, name in  enumerate(self.collumnName):
            df1[name] = df1['course'].str.get(idx)
        df1=df1.drop(['course'], axis='columns')
        self.df = pd.concat([self.df, df1], axis=0)

result = Cleaning()
df1 = result.open_json("데이터사이언스융합전공", "2019학년도 2학기")
df1 = result.cleaning(df1)
result.make_df(df1)
df2 = result.open_json("디자인학과", "2020학년도 1학기")
df2 = result.cleaning(df2)
result.make_df(df2)
engine = create_engine("mysql+pymysql://root:1234@localhost:3306/dsc3037", encoding='utf-8')
conn = engine.connect()
result.df.to_sql(name ="skku_subject",con=engine ,if_exists='append',index = False)
conn.close()
