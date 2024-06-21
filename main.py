from lib.liepin import LiePin
from lib._51job import _51Job
from lib.boss import Boss
from lib.bole import BoLe
from lib.niuke import NiuKe

import signal
import os

if __name__ == '__main__':
    """
    记得关闭excel文件再运行
    """
    job_name = 'python'

    # # 猎聘
    # try:
    #     liepin = LiePin(
    #         job_name='',
    #         pubTime='30',
    #         job_salary='10$20',
    #         job_experience='1',
    #         job_degree='040',
    #         ignore_job=['教师','老师','销售','保险','消防','前台','客服','营销','售后','管培生','助理','经理','硕士','博士','商务'],
    #         ignore_edu=['急聘','1-3年','3-5年','5-10年','2个月','1年以下','3年以上','10年以上'],
    #         ignore_area=['北京','上海'],
    #         ignore_salary=['面议','[0-','[1-','[2-','[3-','[4-','[5-','[6-','[7-','[8-','[9-','100-250元/天','200-300元/天'],
    #         ignore_job_require=['硕士学历','硕士及以上学历','硕士以上学历','博士学历','博士及以上学历','博士以上学历','985','211','出差'],
    #         login_in=True,
    #         overlap=False
    #     )
    #     liepin.run()
    # except: os.kill(os.getpid(), signal.SIGINT)

    # boss直聘
    try:
        boss = Boss(
            job_name=job_name,
            job_salary=['404','405','406','407'],
            # ignore_job=['教师', '老师', '销售', '保险', '消防', '前台', '客服', '营销', '售后', '管培生', '助理','经理', '硕士', '博士', '商务'],
            # ignore_edu=['急聘', '1-3年', '3-5年', '5-10年', '2个月', '1年以下', '3年以上', '10年以上'],
            # ignore_area=['北京', '上海'],
            # ignore_salary=['面议', '[0-', '[1-', '[2-', '[3-', '[4-', '[5-', '[6-', '[7-', '[8-', '[9-', '100-250元/天', '200-300元/天'],
            # ignore_job_require=['硕士学历', '硕士及以上学历', '硕士以上学历', '博士学历', '博士及以上学历', '博士以上学历', '985', '211', '出差'],
            ignore_job=[],
            ignore_edu=[],
            ignore_area=[],
            ignore_salary=[],
            ignore_job_require=[],
            login_in=False
        )
        boss.total_run()
    except Exception as e:
        print("main error:")
        print(e)
        os.kill(os.getpid(), signal.SIGINT)

    # 牛客网
    # try:
    #     niuke = NiuKe(job_name='C++')
    #     niuke.run()
    # except: os.kill(os.getpid(), signal.SIGINT)

    # 51job(前程无忧)
    # try:
    #     _51job = _51Job(
    #         job_name='C++',
    #         job_salary='07',
    #         job_experience='01',
    #         job_degree='04',
    #         ignore_job=['教师', '老师', '销售', '保险', '消防', '前台', '客服', '营销', '售后', '管培生', '助理','经理', '硕士', '博士', '商务'],
    #         ignore_edu=['急聘', '1-3年', '3-5年', '5-10年', '2个月', '1年以下', '3年以上', '10年以上'],
    #         ignore_area=['北京', '上海'],
    #         ignore_salary=['面议', '[0-', '[1千-', '[2千-', '[3千-', '[4千-', '[5千-', '[6千-', '[7千-', '[8千-', '[9千-', '100-250元/天', '200-300元/天'],
    #         ignore_job_require=['硕士学历', '硕士及以上学历', '硕士以上学历', '博士学历', '博士及以上学历', '博士以上学历', '985', '211', '出差', '重点大学'],
    #         login_in=True,
    #         overlap=False
    #     )
    #     _51job.run()
    # except: os.kill(os.getpid(), signal.SIGINT)

    # # 伯乐校招
    # try:
    #     bole = BoLe(
    #         job_name='',
    #         job_salary='5000-10000',
    #         job_degree='3',
    #         ignore_job=['教师', '老师', '销售', '保险', '消防', '前台', '客服', '营销', '售后', '管培生', '助理','经理', '硕士', '博士', '商务'],
    #         ignore_edu=['急聘', '1-3年', '3-5年', '5-10年', '2个月', '1年以下', '3年以上', '10年以上'],
    #         ignore_area=['北京', '上海'],
    #         ignore_salary=['面议', '[0-', '[1000-', '[2000-', '[3000-', '[4000-', '[5000-', '[6000-', '[7000-', '[8000-', '[9000-', '100-250元/天', '200-300元/天'],
    #         ignore_job_require=['硕士学历', '硕士及以上学历', '硕士以上学历', '博士学历', '博士及以上学历', '博士以上学历', '985', '211', '出差'],
    #         login_in=True,
    #         username='', # 手机号
    #         password='',
    #         overlap=False
    #     )
    #     bole.run()
    # except: os.kill(os.getpid(), signal.SIGINT)
