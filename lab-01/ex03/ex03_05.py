def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for Item in lst :
        if Item in count_dict :
            count_dict[Item] +=1
            else:
                count_dict[Item] =1
                return count_dict

                # Nhập danh sách từ người dùng
                input_string = input("Nhập danh sách các từ , cách nhau bằng dấu cách:")
                world_list = input_string.split()

                #Sử dụng hàm và in kết quả
                dem_so_lan_xuat_hien = dem_so_lan_xuat_hien(world_list)
                print("Số lần xuất hiện của các phần tử:", dem_so_lan_xuat_hien)