import os
pair_count_str=input("Enter Number of parenthese pair you want inn your code")
pair_count=int(pair_count_str)
def expression_maker(pair_count):
        expression_p='(2)'
        if(pair_count==1):
                return expression_p
        while_var=0
        while(while_var<pair_count):
                expression_p='('+expression_p+'+2)'
                while_var+=1
        return expression_p

        
def code_replacer_and_new_saver(pair_count):
        print(os.getcwd())
        file_open=open('code_template.py','r')
        file_read=file_open.read()
        print('template_file_loaded')
        expression_p=expression_maker(pair_count)
        new_file_read=file_read.replace('//to_be_replaced',expression_p)
        file_open.close()
        print('template_file_edited')
        file_save=open('edited_code.py', "a+",encoding="utf-8")
        file_save.write(new_file_read)
        file_save.close()
        print('templlate_file_saved')   
        

code_replacer_and_new_saver(pair_count)
