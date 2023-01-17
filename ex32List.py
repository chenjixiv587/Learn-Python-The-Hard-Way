ele1 = [1, 3, 5, 4, 3, 5]
# append(element)在列表中添加元素element 是什么就添加什么
ele1.append(3)
ele1.append("hello")
ele1.append([4, 5, 6, 8])
print(ele1)
# index(ele) 求元素所在的第一个位置  范围 是 左闭右开
print(ele1.index(5, 3))
# ------------------------
ele2 = ["hello", "world"]
# extend(ele) 添加参数，必须是可迭代对象 添加的时候 会拆开来加入
ele2.extend("iamchenwei")
ele2.extend(["we", "see", "you"])
print(ele2)

# -----------------------
ele3 = ["hello", "world", "boy"]
ele3.insert(0, "insert")
ele3.insert(len(ele3), "last")
ele3.remove("hello")
print(ele3)

# -------------------------------

ele4 = [1, 3, 5, 7, 8, 9, 2, 6, 7]
ele4.sort()
print(ele4)
# print(sorted(ele4))
