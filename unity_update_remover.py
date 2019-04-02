import os



def main():
    path = input("enter Assets path: ")

    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith("cs"):

                try:
                    with open(dirpath + '/' + filename,'r+') as csfile:
                        lines = csfile.readlines()

                        has_update = False
                        update_start_line = 0
                        update_end_line = 0
                        has_comment = False
                        for i, line in enumerate(lines):
                            if "// Update is called" in line:
                                has_comment = True

                            if"void Update" in line:
                                has_update = True
                                update_start_line = i
                            # if has_update and "{" in line:

                            if has_update and "}" in line:
                                update_end_line = i
                                break

                        if has_update:

                            update_lines = lines[update_start_line:update_end_line+1]
                            # 빈 업데이트문 일 시
                            updates = "".join(update_lines).replace('void','').replace('()','').replace('\n','').\
                                replace(' ','').replace('\t','').replace('Update','').replace('public','').replace('private','')

                            if updates == "{}":
                                print(filename,"has empty update")
                                csfile.seek(0)
                                _lines = lines[:]
                                _lines[update_start_line -1 * has_comment:update_end_line+1:] = []
                                csfile.writelines(_lines)
                                csfile.truncate()

                except Exception as ex:
                    print(filename, ex)


if __name__ == '__main__':
    main()