# from DrissionPage import ChromiumPage
# from openpyxl import load_workbook, Workbook
# from urllib.parse import quote
#
# import time

"""
智联招聘 - 留档案例
需要登录才能查看全部内容
"""
# job_name = 'C++'
# url = f'https://sou.zhaopin.com/?jl=763&kw={quote(job_name)}&p=1'
# page = ChromiumPage()
# page.get(url)
# while True:
#     time.sleep(0.1)
#     try:
#         # 多此一举，屏蔽滑动验证
#         page.run_js('Object.defineProperties(navigator,{webdriver:{get:()=>false}})')
#     except: pass
#
#     box = page.ele('x://div[@class="positionlist"]').children()
#     for card in box:
#         job_name = card.ele('x://a[contains(@class,"jobinfo__name")]').text
#         job_salary = card.ele('x://p[@class="jobinfo__salary"]').text
#
#         job_tags = []
#         try:
#             for each in card.ele('x://div[@class="jobinfo__tag"]').children():
#                 job_tags.append(each.text)
#         except: pass
#
#         job_area = card.ele('x://img[@class="jobinfo__other-info-location-image"]').next().text
#         job_company = card.ele('x://a[contains(@class,"companyinfo__name")]').text
#
#         job_company_tags = []
#         try:
#             for each in card.ele('x://div[contains(@class,"companyinfo__tag")]').children():
#                 job_company_tags.append(each.text)
#         except: pass
#
#         job_content = ''
#         job_link = ''
#         try:
#             card.ele('x://div[@class="jobinfo__top"]').click()
#             tab = page.latest_tab
#             job_link = tab.url
#
#             job_info_content = tab.ele('x://div[@class="describtion__detail-content"]')
#             job_content = f'{job_content}{job_info_content.text}'
#             for each in job_info_content.children():
#                 job_content = f'{job_content}{each.text}'
#                 try:
#                     each_child = each.child(timeout=0.1)
#                     while each_child:
#                         job_content = f'{job_content}{each_child.text}'
#                         each_child = each_child.child(timeout=0.1)
#                 except: pass
#             print(f'职位:{job_name},工资:{job_salary},公司名:{job_company},位置:{job_area},详细内容:{job_content},招聘页面:{job_link}')
#             time.sleep(0.65)
#             tab.close()
#         except: pass
#         time.sleep(0.1)
#
#     next_page = page.ele('x://button[contains(@class,"btn soupager__btn"]')
#     if 'disabled' != next_page.attr('disabled'):
#         print("智联招聘 Crawl End")
#         break
#     next_page.click()
# page.close()