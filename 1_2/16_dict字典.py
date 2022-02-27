# dict 字典
# { key: value, key1: value1 .... }

# 已知的可哈希（不可变）的数据类型： int str tuple bool
# 不可哈希（可变）的数据类型  list dict set




# 添加数据
# dict['key'] = value
# dict.setdefault(key, value) key必须是不存在的

# 修改
# dict[key] = value

# 删除
# dict.pop(key) 返回value
# dict.clear()
# del dict[key]

# 查询
# dict[key]  如果key 不存在 报错
# dict.get(key) 如果可以 不存在，返回 None

# 特殊的
# dict.setdefault(key) 在执行完新增流程之后，会根据key查找value


s = [11, 22, 33, 44, 55, 66, 77, 88]
result = {}

for item in s:
    if item > 50:
        if result.get('bigger') == None:
            result['bigger'] = [item]
        else:
            result['bigger'].append(item)
    else:
        if result.get('smaller') == None:
            result['smaller'] = [item]
        else:
            result['smaller'].append(item)
print(result)



for item in s:
    if item > 50:
        result.setdefault('bigger', []).append(item)
    else:
        result.setdefault('bigger', []).append(item)
print(result)



# 字典的循环

# for
for key in result:
    print(key)
    print(result[key])

# keys
# d.keys() 拿到字典的keys

# values
for v in result.values():
    print(v)


# items拿到所有数据 (key, value)
# d.itmes()

# 结构
# a = 10, 20  # 结构元祖
# a, b = (10, 20) 结构元祖

# for key, value in d.items()











