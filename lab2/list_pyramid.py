
def pyramid_list(base_len):
    l = [" "] * base_len
    for i in range(1, base_len+1):
        l[-i] = "*"

        print(l)
        
if __name__ == "__main__":
    pyramid_list(5)