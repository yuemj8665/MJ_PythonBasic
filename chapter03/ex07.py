str1 = 'hello'
str2 = ' '
str3 = 'world'
str4 = '                     hello world           '
str5 = 'korea,usa,japan,china,russia'
str6 = 'KOREA,UAS,JAPAN,CHINA,RUSSIA'

# find()
# 매개 변수 문자(열)을 찾는다. 만약에 없으면 -1를 반환한다.
print('\nfind()-----------------')
print(str1.find('he'))
print(str1.find('lo'))
print(str1.find('ss'))

# count()
# 매개 변수 문자(열) 위치를 앞에서부터 찾는다
print("\ncount()----------------")
print(str1.count('e'))
print(str1.count('l'))

# replace()
# 매개 변수 문자(열)을 치환한다
print('\nreplace()---------------')
print(str3)
print(str3.replace('world','python'))

# startswith()
# 매개 변수 문자(열)로 시작하는지 검사하고, true/false를 반환한다.
print('\nstartswith()------------')
print(str1.startswith('he'))
print(str1.startswith('el'))

# endswith()
# 매개 변수 문자(열)로 끝나는지 검사하고, true/false를 반환한다.
print('\nendswith()------------')
print(str1.endswith('lo'))
print(str1.endswith('ell'))

# strip()
# 문자(열)의 시작부분, 끝부분의 공백을 제거한다.
print('\nstrip()------------')
print(str4)
print(str4.strip())

# split()
# 매개 변수를 이용해서 데이터를 문자(열)로 바꾼다. List반환
print('\nsplit()------------')
print(str5.split(','))

# upper()
# 문자(열)을 모두 대문자롤 변경한다
print('\nupper()------------')
print(str5.upper())

# lower
# 문자(열)을 모두 소문자로 변경한다.
print('\nsplit()------------')
print(str6.lower())