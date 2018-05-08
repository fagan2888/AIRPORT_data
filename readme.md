# 机场拼车数据处理

* 到达时间的统计
        
        位于文件夹data_statistic中
        
        数据使用data文件夹中的all.csv
        
        数据文件为data_set
        
        处理文件为data_statistcal

* 目的地转换为经纬度
 
        使用高德开放平台
        
        主函数gpsspg
        
        输入:一列的目的地名称
        
        输出：标准化的目的地名称+经纬度
        
        输入文件：address_list.txt
        
        输出文件：latlng.csv （编码格式GBK）
        
        process_latlng用来将经纬度数据转变为高德地图数据可视化所要求的数据格式
        
        可用于可视化的文件为：first_part_latlng & sencond_part latlng & tot
        
        （以上文件编码格式为UTF-8）
        
* data文件夹存放数据
