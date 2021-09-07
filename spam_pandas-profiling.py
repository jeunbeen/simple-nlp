# %%
import pandas as pd
import pandas_profiling
data = pd.read_csv('C:/Users/admin/Desktop/spam.csv',encoding='latin1')


# %%
data[:5]


# %%
pr=data.profile_report() # 프로파일링 결과 리포트를 pr에 저장
# data.profile_report() # 바로 결과 보기


# %%
pr.to_file('./pr_report.html') # pr_report.html 파일로 저장


# %%
pr # pr에 저장했던 리포트 출력
