# PYTHON SELF-GENERATE CODE
from msilib.schema import Error
# DATABASE
salesDB = [
    {
        "no_order" : "SA01",
        "item" : "Television",
        "units" : 95,
        "unit_price" : 1198,
        "sales_amount" : 113810
    },
    {
        "no_order" : "SA02",
        "item" : "Home Teather",
        "units" : 50,
        "unit_price" : 500,
        "sales_amount" : 25000
    }]
## ADDITIONAL FUNCTION
## PRINT TABEL PENJUALAN
def header_tabel_penjualan():
    print("|NO\t|NO.ORDER\t|ITEM\t\t\t|UNITS\t|UNIT_PRICE\t|SALES_AMOUNT\t|")

def print_tabel_penjualan_all():
    for i in range(len(salesDB)):
        print(f"|{i}\t|{salesDB[i]['no_order']}\t\t|{salesDB[i]['item']}\t\t|{salesDB[i]['units']}\t|{salesDB[i]['unit_price']}\t\t|{salesDB[i]['sales_amount']}\t\t|")

def print_tabel_penjualan_indexed(i):
    print(f"|{i}\t|{salesDB[i]['no_order']}\t\t|{salesDB[i]['item']}\t\t|{salesDB[i]['units']}\t|{salesDB[i]['unit_price']}\t\t|{salesDB[i]['sales_amount']}\t\t|")
## MENU PILIHAN 1
## REPORT DATA PENJUALAN
def report_data_penjualan():
    while True :
        try : 
            subMenuInput = int(input('''
============================ REPORT DATA PENJUALAN ELEKTRONIK ============================
1. REPORT SELURUH DATA
2. REPORT DATA TERTENTU
3. KEMBALI KE MENU UTAMA

SILAHKAN PILIH SUB MENU REPORT DATA YANG TERSEDIA [1-3] : '''
        ))
        ### MENU PILIHAN 1 - 1
        ### PRINT REPORT SELURUH DATA
            if subMenuInput == 1:
                if len(salesDB) > 0:
                    print("============================ REPORT DATA PENJUALAN ELEKTRONIK ============================\nREPORT DATA PENJUALAN")
                    header_tabel_penjualan()
                    print_tabel_penjualan_all()
                else:
                    print("\nPERHATIAN!! : TIDAK ADA DATA YANG TERSEDIA")
        ### MENU PILIHAN 1 - 2
        ### REPORT DATA TERTENTU INPUT NO_ORDER
            elif subMenuInput == 2:
                if len(salesDB) > 0:
                    primKeyDataInput = (input("\n======================== REPORT DATA PENJUALAN ELEKTRONIK TERTENTU =======================\nSilahkan masukan no. order = ")).upper()
                    keyList = [salesDB[i]["no_order"] for i in range(len(salesDB))]
                    if primKeyDataInput in keyList:
                        indextoShow = (keyList.index(primKeyDataInput))
                        print("\nDATA TERTENTU")
                        header_tabel_penjualan()
                        print_tabel_penjualan_indexed(indextoShow)
                    else:
                        print(f"\nPERHATIAN!! : DATA {primKeyDataInput} TIDAK DITEMUKAN")
                else:
                    print("\nPERHATIAN!! : TIDAK ADA DATA YANG TERSEIDA")
        ### MENU PILIHAN 1 - 3
        ### KEMBALI KE MAIN MENU
            elif subMenuInput == 3:
                break
        ### JIKA MEMASUKAN SELAIN ANGKA UNTUK SUBMENU 1
        except ValueError:
            print("\nPERHATIAN_SUB_MENU_1!! : AGAR PILIH SESUAI OPSI YANG TERSEDIA ")
## MENU PILIHAN 2
## MENAMBAHKAN DATA PENJUALAN
def add_data_penjualan():
    while True :
        try:
            subMenuInput = int(input('''
============================= ADD DATA PENJUALAN ELEKTRONIK ============================
1. TAMBAH DATA PENJUALAN
2. KEMBALI KE MENU UTAMA

SILAHKAN PILIH SUB MENU ADD DATA YANG TERSEDIA [1-2] : '''
        ))
        ### MENU PILIHAN 2 - 1
        ### MENAMBAHKAN DATA PENJUALAN
            if subMenuInput == 1:
                print("\n============================= ADD DATA PENJUALAN ELEKTRONIK ============================")
                print("REPORT DATA PENJUALAN EKSISTING")
                header_tabel_penjualan()
                print_tabel_penjualan_all()
                print("\nUPDATE DATA INPUT")
                primKeyDataInput = (input("Silahkan masukan no. order = ")).upper()
                keyList = [salesDB[i]["no_order"] for i in range(len(salesDB))]
                if primKeyDataInput in keyList:
                    print(f"\nPERHATIAN!! : NO ORDER {primKeyDataInput} SUDAH ADA")
                else:
                    newItem = (input("Silahkan masukan item = ")).title()
                    while True:
                        newUnits = input("Silahkan masukan jumlah penjualan = ")
                        if newUnits.isnumeric():
                            break
                        else:
                            print("\nPERHATIAN!! : TOLONG HANYA MASUKAN ANGKA\n")
                    while True:
                        newUnitPrice = input("Silahkan masukan harga satuan = ")
                        if newUnitPrice.isnumeric():
                            break
                        else:
                            print("\nPERHATIAN!! : TOLONG HANYA MASUKAN ANGKA\n")
                    while True:
                        newTotalSale = input("Silahkan masukan total penjualan = ")
                        if newTotalSale.isnumeric():
                            break
                        else:
                            print("\nPERHATIAN!! : TOLONG HANYA MASUKAN ANGKA\n")
                    #### MENAMPILKAN OPSI UNTUK MENYIMPAN DATA
                    while True:
                        saveNewData = (input("Apakah data akan disimpan (y/n) ? = ")).upper()
                        if saveNewData == "Y":
                            salesDB.append({
                                    "no_order" : primKeyDataInput,
                                    "item" : newItem,
                                    "units" : int(newUnits),
                                    "unit_price" : int(newUnitPrice),
                                    "sales_amount" : int(newTotalSale)
                                })
                            print(f"\nNOTIFIKASI => DATA {primKeyDataInput} TERSIMPAN\n")
                            print("============================= REPORT DATA PENJUALAN UPDATE =============================")
                            header_tabel_penjualan()
                            print_tabel_penjualan_all()
                            break
                        elif saveNewData == "N":
                            break  
        ### MENU PILIHAN 2 - 2
        ### KEMBALI KE MAIN MENU
            elif subMenuInput == 2:
                break
        ### JIKA MEMASUKAN SELAIN ANGKA UNTUK SUBMENU 2
        except ValueError:
            print("\nPERHATIAN_SUB_MENU_2_1!! : AGAR PILIH SESUAI OPSI YANG TERSEDIA ")
            print("PERHATIAN_SUB_MENU_2_1!! : AGAR MELAKUKAN INPUT YANG BENAR ")
## MENU PILIHAN 3
## UPDATE DATA PENJUALAN
def update_data_penjualan():
    while True :
        try : 
            subMenuInput = int(input('''
============================ UPDATE DATA PENJUALAN ELEKTRONIK ============================
1. UPDATE DATA PENJUALAN
2. KEMBALI KE MENU UTAMA

SILAHKAN PILIH SUB MENU UPDATE DATA YANG TERSEDIA [1-2] : '''
        ))
        ### MENU PILIHAN 3 - 1
        ### UPDATE DATA PENJUALAN
            if subMenuInput == 1:
                print("\n============================ UPDATE DATA PENJUALAN ELEKTRONIK ============================")
                print("\nPILIHAN REPORT DATA PENJUALAN UNTUK DIUPDATE")
                header_tabel_penjualan()
                print_tabel_penjualan_all()
                primKeyDataInput = (input("\nSilahkan masukan no. order untuk diupdate = ")).upper()
                keyList = [salesDB[i]["no_order"] for i in range(len(salesDB))]
                if primKeyDataInput in keyList:
                    indextoUpdt = (keyList.index(primKeyDataInput))
                    print("\n===================================== DATA TO UPDATE =====================================")
                    print("|NO.ORDER\t|ITEM\t\t\t|UNITS\t|UNIT_PRICE\t|SALES_AMOUNT\t|")
                    print("|{}\t\t|{}\t\t|{}\t|{}\t\t|{}\t\t|\n".format(
                        salesDB[indextoUpdt]['no_order'],
                        salesDB[indextoUpdt]['item'],
                        salesDB[indextoUpdt]['units'],
                        salesDB[indextoUpdt]['unit_price'],
                        salesDB[indextoUpdt]['sales_amount']))
                    while True :
                        checkerToUpdate1 = (input("Apakah ingin lanjut mengupdate data (y/n) ? = ")).upper()
                        if checkerToUpdate1 == "Y":
                            while True:
                                keyToUpdate = (input("Masukan kolom / keterangan yang ingin diupdate = ")).lower()
                                if keyToUpdate == "units" or keyToUpdate == "unit_price" or keyToUpdate == "sales_amount" or keyToUpdate == "item":
                                    break
                                else:
                                    print("\nPILIHAN PARAMETER YANG TERSEDIA : ITEM, UNITS, UNIT_PRICE, SALES_AMOUNT")
                                    print("PERHATIAN!! : NO_ORDER TIDAK DAPAT DIRUBAH\n")
                            updateValue = (input(f"silahkan masukan {keyToUpdate} baru = ")).title()
                            while True : 
                                checkerToUpdate2 = (input("Apakah ingin lanjut mengupdate data (y/n) ? = ")).upper()
                                if checkerToUpdate2 == "Y" or checkerToUpdate2 == "N":
                                    break
                            if checkerToUpdate2 == "Y":
                                if updateValue.isnumeric():
                                    updateValue = int(updateValue)
                                else:
                                    updateValue = str(updateValue)
                                salesDB[indextoUpdt][keyToUpdate] = updateValue
                                print(f"\nNOTIFIKASI => DATA {primKeyDataInput} UPDATED")
                                print("\n============================= REPORT DATA PENJUALAN UPDATE =============================")
                                header_tabel_penjualan()
                                print_tabel_penjualan_all()
                                break
                            elif checkerToUpdate2 == "N":
                                print(f"\nPERHATIAN!! : DATA {primKeyDataInput} TIDAK DIUPDATE")
                                break
                        elif checkerToUpdate1 == "N":
                            print(f"\nPERHATIAN!! : DATA {primKeyDataInput} TIDAK DIUPDATE")
                            break
                elif not (primKeyDataInput in keyList):
                    print(f"\nPERHATIAN!! : DATA {primKeyDataInput} TIDAK DITEMUKAN")
        ### MENU PILIHAN 3 - 2
        ### KEMBALI KE MAIN MENU
            elif subMenuInput == 2:
                break
        ### JIKA MEMASUKAN SELAIN ANGKA UNTUK SUBMENU 3
        except ValueError:
            print("\nPERHATIAN_SUB_MENU_3!! : AGAR PILIH SESUAI OPSI YANG TERSEDIA ")     
## MENU PILIHAN 4
## MENGHAPUS DATA PENJUALAN
def del_data_penjualan():
    while True :
        try : 
            subMenuInput = int(input('''
============================ DELETE DATA PENJUALAN ELEKTRONIK ============================
1. HAPUS DATA PENJUALAN
2. KEMBALI KE MENU UTAMA

SILAHKAN PILIH SUB MENU DELETE DATA YANG TERSEDIA [1-2] : '''
        ))
        ### MENU PILIHAN 4 - 1
        ### OPSI MENGHAPUS DATA
            if subMenuInput == 1:
                print("\n============================ DELETE DATA PENJUALAN ELEKTRONIK ============================")
                print("PILIHAN REPORT DATA PENJUALAN UNTUK DI DELETE")
                header_tabel_penjualan()
                print_tabel_penjualan_all()     
                primKeyDataInput = (input("\nSilahkan masukan no. order untuk dihapus = ")).upper()
                keyList = [salesDB[i]["no_order"] for i in range(len(salesDB))]
                if primKeyDataInput in keyList:
                    indexToDelete = (keyList.index(primKeyDataInput))
                    while True :
                        checkerToDel = (input(f"Apakah data {primKeyDataInput} akan dihapus (y/n) ? = ")).upper()
                        if checkerToDel == "Y":
                            del salesDB[indexToDelete]
                            print(f"\nNOTIFIKASI => DATA {primKeyDataInput} DELETED")

                            print("============================= REPORT DATA PENJUALAN UPDATE =============================")
                            header_tabel_penjualan()
                            print_tabel_penjualan_all()
                            break
                        elif checkerToDel == "N":
                            print(f"\nNOTIFIKASI => DATA {primKeyDataInput} TIDAK DIHAPUS")
                            break
                elif not (primKeyDataInput in keyList):
                    print(f"\nPERHATIAN!! : DATA {primKeyDataInput} TIDAK DITEMUKAN")
        ### MENU PILIHAN 4 - 2
        ### KEMBALI KE MAIN MENU
            elif subMenuInput == 2:
                break
        ### JIKA MEMASUKAN SELAIN ANGKA UNTUK SUBMENU 4
        except ValueError:
            print("\nPERHATIAN_SUB_MENU_4 !! : AGAR PILIH SESUAI OPSI YANG TERSEDIA ")
# MENU UTAMA
while True :
    try: 
        mainMenuInput = int(input('''
============================ RECORD PENJUALAN TOKO ELEKTRONIK ============================
1. REPORT DATA PENJUALAN ELEKTRONIK
2. MENAMBAHKAN DATA PENJUALAN
3. UPDATE DATA PENJUALAN
4. MENGHAPUS DATA PENJUALAN
5. EXIT

SILAHKAN PILIH MENU YANG TERSEDIA [1-5] : '''
        ))
        if mainMenuInput == 1:
            report_data_penjualan()
        elif mainMenuInput == 2:
            add_data_penjualan()
        elif mainMenuInput == 3:
            update_data_penjualan()
        elif mainMenuInput == 4:
            del_data_penjualan()
        elif mainMenuInput == 5:
            while True:
                exitapps = input("Yakin ingin keluar dari aplikasi (y/n)? = ").upper()
                if exitapps == "Y" or exitapps == "N":
                    break
            if exitapps == "Y":
                print("Terima kasih telah menggunakan Apps kami")
                break
        else:
            print("\nPERHATIAN!! : PILIHAN YANG ANDA MASUKAN SALAH")
    except ValueError:
        print("\nPERHATIAN_MAIN_MENU!! : AGAR PILIH SESUAI OPSI YANG TERSEDIA ")