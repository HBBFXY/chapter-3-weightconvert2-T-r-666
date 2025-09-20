# 在这个文件里编写代码
# 假设当前在地球上的体重（单位：kg）
current_weight=60
moon_weight_change=0.165
yearly_gain=0.5
print("未来10年地球和月球上的体重变化：")
for year in range(1, 11):
    earth_weight=current_weight+yearly_gain*year
    moon_weight=earth_weight*moon_weight_change
    print("第{}年,在地球上体重{:.2f}kg,月球上体重{:.2f}kg".format(year,earth_weight,moon_weight))
