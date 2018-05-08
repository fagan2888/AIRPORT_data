# 将目的地名称转换为经纬度数据

使用高德开放平台

主函数gpsspg

输入:一列的目的地名称

输出：标准化的目的地名称+经纬度

输入文件：address_list.txt

输出文件：latlng.csv （编码格式GBK）

process_latlng用来将经纬度数据转变为高德地图数据可视化所要求的数据格式

可用于可视化的文件为：first_part_latlng & sencond_part latlng & tot

（以上文件编码格式为UTF-8）