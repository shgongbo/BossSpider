# from DrissionPage import ChromiumPage
# from openpyxl import load_workbook, Workbook
# from urllib.parse import quote
#
# import time
# import os
# import signal
#
# # 薪资 - salary
# """
# 不限：''
# 2k以下：'2k以下'
# 2k-5k：'2k-5k'
# 5k-10k：'5k-10k'
# 10k-15k：'10k-15k'
# 15k-25k：'15k-25k'
# 25k-50k：'25k-50k'
# 50k以上：'50k以上'
# """
#
# class LaGou():
#     def __init__(self,job_name='',job_salary='07',
#         ignore_job=[],ignore_edu=[],ignore_area=[],ignore_salary=[],ignore_job_require=[],
#         overlap=False,login_in=False):
#         self.login_in = login_in
#         self.ignore_job = ignore_job
#         self.ignore_edu = ignore_edu
#         self.ignore_area = ignore_area
#         self.ignore_salary = ignore_salary
#         self.ignore_job_require = ignore_job_require
#
#         self.query = f'https://www.lagou.com/wn/jobs?yx={quote(job_salary)}&px=new&cl=false&fromSearch=true&labelWords=sug&suginput={quote(job_name)}&kd={quote(job_name)}&pn=1&gj={quote("不要求")}'
#         file_name = '../output/lagou_crawl_output.xlsx'
#
#         if overlap:
#             counter = 1
#             while os.path.exists(file_name):
#                 file_name = f'../output/lagou_crawl_output_{counter}.xlsx'
#                 counter += 1
#         elif os.path.exists(file_name): os.remove(file_name)
#
#         self.file_path = file_name
#
#         wb = Workbook()
#         ws = wb.active
#         row = ws.max_row
#
#         ws.cell(row=row, column=1, value='职位')
#         ws.cell(row=row, column=2, value='工资')
#         ws.cell(row=row, column=3, value='公司名')
#         ws.cell(row=row, column=4, value='位置')
#         ws.cell(row=row, column=5, value='详细内容')
#         ws.cell(row=row, column=6, value='招聘页面')
#
#         wb.save(self.file_path)
#         wb.close()
#
#     def run(self):
#         page = ChromiumPage()
#
#         # 微信扫码登录
#         if self.login_in:
#             print("login.....")
#             page.get('https://passport.lagou.com/login/login.html?msg=needlogin')
#             page.ele('x://div[@class="qr_code_img pc-form-pane"]').click()
#             time.sleep(25)
#
#         page.get('https://www.lagou.com/wn/zhaopin?fromSearch=true&kd=&city=%E5%B9%BF%E5%B7%9E')
#         page.get(self.query)
#
#         while True:
#             time.sleep(0.5)
#             # 多此一举，屏蔽滑动验证
#             try: page.run_js('Object.defineProperties(navigator,{webdriver:{get:()=>false}})')
#             except: pass
#
#             box = page.ele('x://div[@id="jobList"]').child()
#             for card in box.children():
#                 continue_flag = False
#                 job_info_combined = card.ele('x://a[@id="openWinPostion"]').text
#                 # 职位
#                 job_name = job_info_combined[0:job_info_combined.rfind('[')]
#                 for each in self.ignore_job:
#                     if each in job_name:
#                         continue_flag = True
#                         break
#                 if continue_flag: continue
#                 print(f'{job_name}\n')
#
#                 # 薪资
#                 job_salary = card.ele('x://span[contains(@class,"money__")]').text
#                 job_salary = f'[{job_salary}]'
#                 for each in self.ignore_salary:
#                     if each in job_salary:
#                         continue_flag = True
#                         break
#                 if continue_flag: continue
#
#                 # 学历
#                 job_tags = ''
#                 try: job_tags += card.ele('x://div[contains(@class,"p-bom__")]').text
#                 except: pass
#
#                 for each in self.ignore_edu:
#                     if each in job_tags:
#                         continue_flag = True
#                         break
#                 if continue_flag: continue
#
#                 # 地区
#                 job_area = job_info_combined[job_info_combined.rfind('[') + 1:job_info_combined.rfind(']')]
#                 for each in self.ignore_area:
#                     if each in job_area:
#                         continue_flag = True
#                         break
#                 if continue_flag: continue
#
#                 job_company = card.ele('x://div[contains(@class,"company-name")]').child().text
#                 job_company_tags = ''
#                 try: job_company_tags += card.ele('x://div[contains(@class,"industry__")]',timeout=0.15).text
#                 except: pass
#
#                 job_content = ''
#                 job_link = ''
#                 try:
#                     element = card.ele('x://a[@id="openWinPostion"]')
#                     page.run_js("arguments[0].style.width='100px'; arguments[0].style.height='100px';", element)
#
#                     card.ele('x://a[@id="openWinPostion"]').click(by_js=True)
#                     tab = page.latest_tab
#                     job_link = tab.url
#
#                     try:
#                         for each in tab.ele('x://h3[@class="position-tags"]',timeout=0.15).children():
#                             job_content = f'{job_content}/{each.raw_text}'
#                     except: pass
#
#                     if job_content: job_content += '\n'
#                     for label in tab.ele('x://dl[@class="job_detail"]').children():
#                         for each in label.children(timeout=0.15):
#                             job_content = f'{job_content}{each.text}'
#
#                     for each in self.ignore_job_require:
#                         if each in job_content:
#                             continue_flag = True
#                             break
#
#                     time.sleep(0.4)
#                     if continue_flag:
#                         tab.close()
#                         continue
#
#                     print(f'职位:{job_name},工资:{job_salary},公司名:{job_company},位置:{job_area},详细内容:\n{job_content},招聘页面:{job_link}\n')
#                     tab.close()
#                 except: pass
#
#                 time.sleep(0.15)
#                 wb = load_workbook(self.file_path)
#                 ws = wb.active
#                 row = ws.max_row + 1
#
#                 ws.cell(row=row, column=1, value=job_name)
#                 ws.cell(row=row, column=2, value=job_salary)
#                 ws.cell(row=row, column=3, value=job_company)
#                 ws.cell(row=row, column=4, value=job_area)
#                 ws.cell(row=row, column=5, value=job_content)
#                 ws.cell(row=row, column=6, value=job_link)
#
#                 wb.save(self.file_path)
#                 wb.close()
#
#             next_page = page.ele('x://ul[@class="lg-pagination"]').children()[-1]
#             if 'true' == next_page.attr('aria-disabled'):
#                 print('拉钩招聘 Crwal End')
#                 break
#             next_page.click()
#
#         page.close()
#
#
# if __name__ == '__main__':
#     try:
#         LaGou = LaGou(
#             job_name='',
#             job_salary='10k-15k',
#             ignore_job=['教师', '老师', '销售', '保险', '消防', '前台', '客服', '营销', '售后', '管培生', '助理','经理', '硕士', '博士', '商务'],
#             ignore_edu=['急聘', '1-3年', '3-5年', '5-10年', '2个月', '1年以下', '3年以上', '10年以上'],
#             ignore_area=[],
#             ignore_salary=['面议', '[0-', '[1-', '[2-', '[3-', '[4-', '[5-', '[6-', '[7-', '[8-', '[9-', '100-250元/天', '200-300元/天'],
#             ignore_job_require=['硕士学历', '硕士及以上学历', '硕士以上学历', '博士学历', '博士及以上学历', '博士以上学历', '985', '211', '出差'],
#             login_in=True
#         )
#         LaGou.run()
#     except: os.kill(os.getpid(), signal.SIGINT)