def my_print(txt):
    print(txt)

msg_template = """
Hello {name},
Thanks for joining"""

#Creates a var called my_msg and uses the argument my_name to format
#the template, adding the new name to it and returning it with the
#new name
def format_msg(my_name):
    my_msg = msg_template.format(name=my_name)
    return my_msg
