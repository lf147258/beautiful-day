#物品库存系统
stores={"apple":50,"pear":60,"bnana":90,"orange":40,"lemon":30}
print("欢迎登陆物品查询系统！")
username=input("请输入用户名:")
password=input("请输入密码:")
if username!="lee" or password!="147258":
	print("您输入的用户名或密码错误！请从新输入：")
else:
	print("恭喜您成功登入！")
	menu=["1.查询","2.修改","3.录入","4.删除","5.列表","6.退出"]
	for i in menu:
	    print(i)
	oper=int(input("请输入操作数："))
	if oper==1:
		name=input("请输入物品名：")
		if name in stores:
			print("{0}的数量为{1}个".format(name,stores[name]))
		else:
			print("此物品暂无！")
	if oper==2:
		name1=input("请输入需要修改的物品名:")
		if name1 in stores:
			a=int(input("请输入需要修改为："))
			stores[name1]=a
			print("{0}修改后，数量为{1}个".format(name1,stores[name1]))
		else:
			print("输入的商品错误！")
	if oper==3:
		name2=input("请输入新的物品名：")
		stores[name2]=int(input("数量为："))
		print("{0},{1}个".format(name2,stores[name2]))
	if oper==4:
		name3=input("请输入需要删除的物品：")
		if name3 in stores:
			stores.pop(name3)
		else:
			print("库存中无此商品！")
	if oper==6:
		print("您已退出系统！")
	if oper==5:
		for k in stores:
			print("{0}的数量为{1}".format(k,stores[k]))

			







   
