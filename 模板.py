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

    

    # 关闭浏览器连接
    browser.close()


# 使用 Playwright 启动自动化
with sync_playwright() as playwright:
    run(playwright)
