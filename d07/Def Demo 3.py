def calc(id, no, *score, **info):
    sum = sum(score)
    print('%d 姓名:%s 座號:%d 總分:%d 學員資料:%s' % (id, info.get('name')
                                            ,no,sum(score),info))

if __name__ =='__main__':
    calc(1,5100,90,80,name='Atom',age=18)