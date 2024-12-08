from playwright.sync_api import sync_playwright
import subprocess


# 设置 Edge 浏览器路径和调试端口
edge_path = r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
debugging_port = "--remote-debugging-port=9222"

# 启动 Edge 浏览器并开放调试端口
command = f'"{edge_path}" {debugging_port}'
subprocess.Popen(command, shell=True)


def run(playwright):
    # 通过 CDP (Chrome DevTools Protocol) 连接到 Edge 浏览器
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")

    # 获取默认的上下文并打开新页面
    context = browser.contexts[0]  # 获取现有的上下文
    page = context.new_page()  # 在该上下文中创建新的页面

    page.goto("https://www.exmple.com/")

    page.wait_for_load_state("networkidle")

    path = r"D:/*/*/" # 修改为你的保存路径
    title_list = []
    for i in range(7, 38):
        title_url = page.locator(f'xpath=//*[@id="list"]/dl/dd[{i}]/a').get_attribute(
            "href"
        ) # 获取每个标题的 url

        title_list.append(url + title_url) # 拼接成完整的 url

    for url in title_list:
        page.goto(url)
        page.wait_for_load_state("networkidle")
        
        title = page.locator(
            f'xpath=//*[@id="wrapper"]/div[4]/div/div[2]/h1'
        ).inner_text()

        text = page.locator(f'xpath=//*[@id="content"]').inner_text()

        q = "**********"
        text = text.replace(q, "") # 替换掉不需要的内容

        with open(path + title + ".txt", "w", newline="", encoding="utf-8") as f:
            f.write(text)

    # 关闭浏览器连接
    browser.close()


# 使用 Playwright 启动自动化
with sync_playwright() as playwright:
    run(playwright)
