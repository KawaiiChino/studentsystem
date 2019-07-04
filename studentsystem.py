# -*- coding: utf-8 -*-
#2019/7/2
#chao

import re,os


def menu():
	#输出菜单
	print('''
	------------学生管理系统------------
	|                                  |
	|  ========功能菜单============    |
	|                                  |
	|  1.录入学生信息                  |
	|  2.查找学生信息                  |
	|  3.删除学生信息                  |
	|  4.修改学生信息                  |
	|  5.排序                          |
	|  6.统计学生总人数                |
	|  7.显示所有学生信息              |
	|  0.退出系统                      |
	|                                  |
	|  ============================    |
	|  说明：通过数字或↑↓反向键选择  |
	|                                  |
	------------------------------------''')


def save(studentlist):
	filename = "student.txt"
	try:
		studentinfo= open(filename,'a')
	except Exception as ret:
		studentinfo = open(filename,'w')
	for student in studentlist:
		studentinfo.write(str(student)+"\n")
	studentinfo.close()


def insert():
	mark = True
	studentlist = list()
	while mark:
		name = input("请输入姓名：")
		if not name:
			break
		ID = input("请输入学号：")
		if not ID:
			break
		try :
			math = int(input("请输入数学成绩："))
			python = int(input("请输入Python成绩："))
			C = int(input("请输入C语言成绩："))
		except :
			print("您的输入有误！")
			continue
		student = {"姓名":name,"ID":ID,"math":math,"python":python,"C":C}
		studentlist.append(student)
		inputmark = input("是否继续输入？ （y/n）")
		if inputmark == "y" :
			mark = True
		else :
			mark = False
	save(studentlist)
	print("录入信息完毕！")


def search():
	while True:
		try:
			studentinfo = open("student.txt",'r')
		except :
			print("没有录入学生信息")
		else:
			findinfo = input("请输入查找学生信息或者学号：")
			mark = False
			for line in studentinfo:
				d = dict(eval(line))
				if findinfo == d['姓名'] or findinfo == d['ID']:
					print("您查找的学生信息已找到：")
					print(
						"姓名：%s\n学号：%s\n数学成绩：%d\npython:%d\nC:%d\n" \
						% (d['姓名'], d['ID'], int(d['math']), int(d['python']), int(d['C'])))
					mark = True
				else:
					continue
			if not mark:
				print("查无此人")
			m= input("是否继续查找(y/n)")
			studentinfo.close()
			if m == "y":
				continue
			else:
				break


def delete():
	try:
		studentinfo = open("student.txt",'r')
	except:
		print("没有录入学生信息")
	else:
		studentlist = studentinfo.readlines()
		studentinfo.close()
		if not studentlist:
			print("没有录入学生信息")
		else:
			while True:
				delinfo = input("请输入学生的姓名或者学号：")
				dellist = list()
				for student in studentlist:
					d = dict(eval(student))
					if delinfo == d["姓名"] or delinfo == d["ID"]:
						studentlist.remove(student)
						dellist.append(student)
						print("删除成功")
					else:
						continue
				if not dellist:
					print("没有该学生信息")
				m = input("是否继续删除学生信息：(y/n)")
				if m == "y":
					continue
				else:
					break
			with open("student.txt",'w') as newstudentinfo:
				for leftstudent in studentlist:
					newstudentinfo.write(leftstudent)


def modify():
	if os.path.exists("student.txt"):
		with open("student.txt",'r') as rfile:
			student_old = rfile.readlines()
	else:
		return
	studentid = input("请输入要修改学生ID")
	with open("student.txt",'w') as wfile:
		for student in student_old:
			d = dict(eval(student))
			if d['ID'] == studentid:
				print("找到该学生！")
				while True:
					try:
						d["姓名"] = input("请输入姓名：")
						d["math"] = int(input("math"))
						d["python"] = int(input("python"))
						d["C"] = int(input("C"))
					except :
							print("输入有误！")
					else:
						break
				student = str(d)
				wfile.write(student+"\n")
				print("修改成功")
		else:
			wfile.write(student)
		mark = input("继续修改？（y/n）")
		if mark == "y" :
			modify()


def sort():
	if os.path.exists("student.txt") :
		with open("student.txt") as file:
			student_old = file.readlines()
		student_new = list()
		for list in student_old:
			d = dict(eval(list))
			student_new.append(d)
	else:
		return
	order = input("请选择升序（0）还是降序（1）：")
	ascORdesc = input("请选择（0升序；1降序）：")
	if ascORdesc == "0":  # 按升序排序
		ascORdescBool = False  # 标记变量，为False表示升序排序
	elif ascORdesc == "1":  # 按降序排序
		ascORdescBool = True  # 标记变量，为True表示降序排序
	else:
		print("您的输入有误，请重新输入！")
		sort()
	mode = input("请选择排序方式（1math；2Python；3C；0按总成绩排序）：")
	if mode == "1":
		student_new.sort(key=lambda x: x["math"], reverse=ascORdescBool)
	elif mode == "2":  # 按Python成绩排序
		student_new.sort(key=lambda x: x["python"], reverse=ascORdescBool)
	elif mode == "3":  # 按C语言成绩排序
		student_new.sort(key=lambda x: x["C"], reverse=ascORdescBool)
	elif mode == "0":  # 按总成绩排序
		student_new.sort(key=lambda x: x["math"] + x["python"] + x["C"], reverse=ascORdescBool)
	else:
		print("您的输入有误，请重新输入！")
		sort()


def total():
	if os.path.exists("student.txt"):  # 判断文件是否存在
		with open("student.txt", 'r') as rfile:  # 打开文件
			student_old = rfile.readlines()  # 读取全部内容
			if student_old:
				print("一共有 %d 名学生！" % len(student_old))
			else:
				print("还没有录入学生信息！")
	else:
		print("暂未保存数据信息...")


def show():
	student_new = []
	if os.path.exists("student.txt"):  # 判断文件是否存在
		with open("student.txt", 'r') as rfile:  # 打开文件
			student_old = rfile.readlines()  # 读取全部内容
		for list in student_old:
			student_new.append(eval(list))  # 将找到的学生信息保存到列表中
		if student_new:
			show_student(student_new)
	else:
		print("暂未保存数据信息...")

def show_student(studentList):
    if not studentList:
        print("(o@.@o) 无数据信息 (o@.@o) \n")
        return
    format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format("ID", "姓名", "math", "Python", "C", "总成绩"))
    format_data = "{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    for info in studentList:
        print(format_data.format(info.get("ID"), info.get("姓名"), str(info.get("math")), str(info.get("python")),
                                 str(info.get("C")),
                                 str(info.get("math") + info.get("python") + info.get("C")).center(12)))


def main():
	ctrl = True  # 标记是否退出系统
	while (ctrl):
		menu()
		option = input("请选择：")
		option_str = re.sub("\D","",option)
		if option_str in ['0','1','2','3','4','5','6','7']:
			option_int = int(option_str)
			if option_int == 0 :
				print("您已退出学生信息管理系统")
				ctrl = False
			elif option_int == 1 :
				insert()
			elif option_int == 2 :
				search()
			elif option_int == 3 :
				delete()
			elif option_int == 4 :
				modify()
			elif option_int == 5:
				sort()
			elif option_int == 6:
				total()
			else:
				show()


if __name__ == "__main__":
	main()