import os

os.chdir('files/dir')


# print(os.getcwd())

# for f in os.listdir():
#    
#     f_name, f_ext = os.path.splitext(f)

#     # print(f_name.split('-'))

#     f_title = f_name.split('-')
    
#     if len(os.listdir()) < 6:
#         f_title.pop(1)
        
    
#     f_title.pop(1)
#     f_title.pop(-1)
#     f_title = "-".join(f_title)
#     f_title = f_title.split(" ")
#     f_title.pop(-1)
#     f_title = " ".join(f_title)
#     f_title = f_title.strip(".fyccasd2act")
#     f_title = f_title.split('.')
    
#     if len(f_title) == 2:
#         f_title.pop(-1)
    
#     title_name = f_title[0].split(" ")
#     if len(title_name) == 4:
#         title_name.pop(-1)

    
#     s1, s2, t = title_name
#     new_name = '{}-{}{}{}'.format(s1,s2,t,f_ext)
#     os.rename(f, new_name)


    