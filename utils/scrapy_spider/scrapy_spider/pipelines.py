import os

from ZLSProject.settings import BASE_DIR


class ScrapySpiderPipeline:
    def process_item(self, item, spider):
        zhiliannzhaopin_info = os.path.join(BASE_DIR, "resources", "dataset", "智联招聘.csv")
        with open(zhiliannzhaopin_info, "a+", encoding="utf-8") as f:
            for i in dict(item).items():
                f.write("".join(i[1]) + ",")
            f.write("\n")
        return item

    def open_spider(self, spider):
        zhiliannzhaopin_info = os.path.join(BASE_DIR, "resources", "dataset", "智联招聘.csv")
        with open(zhiliannzhaopin_info, "w", encoding="utf-8") as f:
            f.write("工作名,学历,工作地点,工作时间,工资,公司名,企业人数,企业类型,岗位标签\n")
        print("爬虫开始")

    def close_spider(self, spider):
        print("爬虫结束")
