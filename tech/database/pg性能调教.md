# PostgresSQL 

对象/关系型数据库管理系统


# 1. PostgreSQL 版本

一旦做了合理的实施之后,还可以回过头来对他进行优化

# 2. 数据库硬件

## 2.1 平衡硬件支出

### CPU

top指令查看单个CPU上进程数量,如果进程数量较少,那么可能需要运算速度高的CPU,如果进程数目较多,那么可能需要增加CPU数量

COPY 时PostgreSQL最好的数据导入方法

### 内存

- 如果用户的数据集大小恰好能够容纳这种较小数量的RAM的时候,增加内润并不能提升性能.用户可能需要更快的处理器
- 当在一些数据仓库的环境下,所云心的程序扫描的表大小大于用户可以给其分配的内存大小是,用户需要更快的硬盘而不是增加更多的内存

### 磁盘

#### RAID 0:

同时使用多个硬盘,并行地将数据分散到每个硬盘中进行读写.新能得到线性提升.任何一块磁盘故障,则丢失所有数据

#### RAID 1:

多个副本存储在多块硬盘中,读取操作时性能可能提高

#### RAID 10或RAID 1+0

首先使用成对的磁盘,然后进行RAID 1镜像.然后使用RAID 0对结果集进行分组.既提高性能还允许其中一块硬盘损坏.非常适合写操作频繁的环境

#### RAID 5

介于RAID 0和RAID 1.数据类似RAID 0分片存储在磁盘中,可以提高读取性能,冗余数据存储在校验盘中.用较小的空间浪费来解决磁盘失效的问题.丢失的数据可以用其他磁盘的校验信息计算得出.

# 3. 数据库硬件基准评测

## 3.1 CPU和内存基准评测

## 3.2 磁盘的性能

# 4. 磁盘设置

## 4.1 文件系统最大值

有些文件系统下分区大小不超过2TB

## 4.2 文件系统恢复

利用日志文件系统


## 4.3 Linux文件系统

### ext2 不支持日志

### ext3 增加了日志文件




# 5. 数据库高速缓存内存
# 6. 服务器配置调整
# 7. 日常维护
# 8. 数据库基准评测
# 9. 数据库索引
# 10. 查询优化
# 11. 数据库活动和统计信息
# 12. 监控与趋势预测
# 13. 池化与高速缓存
# 14. 扩展复制
# 15. 数据分区
# 16. 应该避免的一些常见问题