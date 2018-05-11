# 机场拼车数据处理

* 到达时间的统计(data_statistic)
        
        位于文件夹data_statistic中
        
        数据使用data文件夹中的all.csv
        
        数据文件为data_set
        
        处理文件为data_statistcal
        
* 获得各个点之间的距离（get_dist）
        
        get_info获取返回的json response
        
        dist_info_out用以存放json语句
        
        dist_array将返回结果处理为矩阵，分天输出

* 目的地转换为经纬度(get_latlng)
 
        使用高德开放平台
        
        主函数gps_amap & gps_tecent
        
        输入:一列的目的地名称
        
        输出：标准化的目的地名称+经纬度
        
        输入文件：address_list.txt
        
        输出文件：latlng.csv （编码格式GBK）
        
* 将数据进行格式转换以符合高德平台的要求（visual）

        process_latlng用来将经纬度数据转变为高德地图数据可视化所要求的数据格式
        
* 将数据转换为路径并处理为高德需要的格式（show_path）

        输出为carpath

* data文件夹存放数据

        分为总数据final
        
        第一天的数据oneday用来方便测试
