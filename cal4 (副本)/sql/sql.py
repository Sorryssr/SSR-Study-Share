"""
-- cj.cal definition

CREATE TABLE `cal` (
  `门店名称` varchar(100) DEFAULT NULL,
  `门店品牌名称` varchar(100) DEFAULT NULL,
  `总计费` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `登记时间` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



-- cj.calnull definition

CREATE TABLE `calnull` (
  `门店名称` varchar(100) DEFAULT NULL,
  `目的地` varchar(100) DEFAULT NULL,
  `运单号` varchar(100) DEFAULT NULL,
  `收件重量` varchar(100) DEFAULT NULL,
  `计费` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



-- cj.calnullsecond definition

CREATE TABLE `calnullsecond` (
  `面单发放客户` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `单号` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `收件扫描日期` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `揽收业务员` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `客户名称` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `结算客户` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `目的地` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `结算重量` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `应收运费` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- cj.calnullshop definition

CREATE TABLE `calnullshop` (
  `店铺名称` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `寄件人` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `目的地` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `运单号` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `收件重量` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `计费` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



-- cj.`first` definition

CREATE TABLE `first` (
  `录单时间` varchar(255) DEFAULT NULL,
  `运单号` varchar(255) DEFAULT NULL,
  `业务员姓名` varchar(255) DEFAULT NULL,
  `业务员工号` varchar(255) DEFAULT NULL,
  `寄件人` varchar(255) DEFAULT NULL,
  `寄件人电话` varchar(255) DEFAULT NULL,
  `寄件详细地址` varchar(255) DEFAULT NULL,
  `收件人` varchar(255) DEFAULT NULL,
  `收件人电话` varchar(255) DEFAULT NULL,
  `收件详细地址` varchar(255) DEFAULT NULL,
  `目的地` varchar(255) DEFAULT NULL,
  `收件重量` float DEFAULT NULL,
  `录单状态` varchar(255) DEFAULT NULL,
  `录单重量` float DEFAULT NULL,
  `运费` float DEFAULT NULL,
  `计费运费` float DEFAULT NULL,
  `支付金额` float DEFAULT NULL,
  `支付状态` varchar(255) DEFAULT NULL,
  `付款方式` varchar(255) DEFAULT NULL,
  `物品名称` varchar(255) DEFAULT NULL,
  `增值类型` varchar(255) DEFAULT NULL,
  `代收金额` float DEFAULT NULL,
  `优惠券` varchar(255) DEFAULT NULL,
  `订单来源` varchar(255) DEFAULT NULL,
  `单号来源` varchar(255) DEFAULT NULL,
  `店铺名称` varchar(255) DEFAULT NULL,
  `承包区子业务员工号` varchar(255) DEFAULT NULL,
  `是否发货` varchar(255) DEFAULT NULL,
  `发货时间` varchar(255) DEFAULT NULL,
  `门店名称` varchar(255) DEFAULT NULL,
  `门店编码` varchar(255) DEFAULT NULL,
  `门店品牌名称` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- cj.price definition

CREATE TABLE `price` (
  `目的地` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `level1` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `level2` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `level3` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `level4` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- cj.priceshop definition

CREATE TABLE `priceshop` (
  `目的地` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `level1` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `level2` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `level3` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `level4` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- cj.`second` definition

CREATE TABLE `second` (
  `账单归属` varchar(255) DEFAULT NULL,
  `单号` varchar(255) DEFAULT NULL,
  `包号` varchar(255) DEFAULT NULL,
  `收件扫描日期` varchar(255) DEFAULT NULL,
  `揽收业务员` varchar(255) DEFAULT NULL,
  `工号` varchar(255) DEFAULT NULL,
  `客户名称` varchar(255) DEFAULT NULL,
  `结算客户` varchar(255) DEFAULT NULL,
  `运输方式` varchar(255) DEFAULT NULL,
  `产品类型` varchar(255) DEFAULT NULL,
  `目的地` varchar(255) DEFAULT NULL,
  `目的城市` varchar(255) DEFAULT NULL,
  `结算重量` varchar(255) DEFAULT NULL,
  `应收面单费` varchar(255) DEFAULT NULL,
  `应收运费` varchar(255) DEFAULT NULL,
  `修改人` varchar(255) DEFAULT NULL,
  `修改时间` varchar(255) DEFAULT NULL,
  `面单类型` varchar(255) DEFAULT NULL,
  `物品类型` varchar(255) DEFAULT NULL,
  `退件` varchar(255) DEFAULT NULL,
  `问题件` varchar(255) DEFAULT NULL,
  `面单发放客户` varchar(255) DEFAULT NULL,
  `网点收我面单费` varchar(255) DEFAULT NULL,
  `网点收我中转费` varchar(255) DEFAULT NULL,
  `订单来源` varchar(255) DEFAULT NULL,
  `订单编号` varchar(255) DEFAULT NULL,
  `签收状态` varchar(255) DEFAULT NULL,
  `签收网点` varchar(255) DEFAULT NULL,
  `签收时间` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- cj.calsecond definition

CREATE TABLE `calsecond` (
  `面单发放客户` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `面单总数` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `总计费` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `登记时间` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;





"""


"""


"""