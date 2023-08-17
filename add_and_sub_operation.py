import re
input = input("Enter input value : ")
list = re.split(r'',input)
print("List: ",list)
for operator in list:
    print("new",list)
    if operator == "+":
        operator_index = list.index("+")
        print("Operator index value",operator_index)
        input_index1 = operator_index - 1
        print("Index value of the operant before the operator",input_index1)
        input_index2 = operator_index + 1
        print("Index value of the operant after the operator",input_index2)
        input1 = list[input_index1]
        print("value of the operant present before the operator",input1)
        input2 = list[input_index2]
        print("value of the operant present after the operator",input2)
        addition = int(input1) + int(input2)
        print("Addition of two operants are : ",addition)
        del list[input_index1 : input_index2 + 1]
        print("List after poping elements : ",list)
        list.insert(1, addition)
        newlist = list
        print("newlist : ",newlist)
        print("Addition Output : ",addition)
        newlist = list
    for operator in list:
        if operator == "-":
            operator_index = list.index("-")
            print("Operator index value",operator_index)
            input_index1 = operator_index - 1
            print("Index value of the operant before the operator",input_index1)
            input_index2 = operator_index + 1
            print("Index value of the operant after the operator",input_index2)
            input1 = list[input_index1]
            print("value of the operant present before the operator",input1)
            input2 = list[input_index2]
            print("value of the operant present after the operator",input2)
            subtraction = int(input1) - int(input2)
            print("Subtraction of two operants are : ",subtraction)
            print("Subtraction Output : ",subtraction)
            del list[input_index1 : input_index2 + 1]
            print("List after poping elements : ",list)
            list.insert(1, subtraction)
            newlist = list
            
        



    
        