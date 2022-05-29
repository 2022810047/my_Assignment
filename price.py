def shopping(shop_file):
    with open("./data/" + shop_file, mode='r', encoding='utf-8') as f: # 단, 파일이 data폴더 안에 있어야 함
      menu_list = []
      line_num = 0
      while True:
          the_line = f.readline()
          if not the_line: break
          if line_num <= 1:
              line_num += 1
              continue
          menu_list.append(the_line.split())
          line_num += 1
    shop_dict = {}
    for a_menu in menu_list:
        new_menu = {a_menu[0]: a_menu[1]}
        shop_dict.update(new_menu)
    return shop_dict



def item_price(shop_file, item):
    def shopping(shop_file):
      with open("./data/" + shop_file, mode='r', encoding='utf-8') as f:
        menu_list = []
        line_num = 0
        while True:
            the_line = f.readline()
            if not the_line: break
            if line_num <= 1:
                line_num += 1
                continue
            menu_list.append(the_line.split())
            line_num += 1
      shop_dict = {}
      for a_menu in menu_list:
          new_menu = {a_menu[0]: a_menu[1]}
          shop_dict.update(new_menu)
      return shop_dict
    price_dict = shopping(shop_file)
    result = price_dict[item]
    return result
