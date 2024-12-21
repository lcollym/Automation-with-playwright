from playwright.sync_api import sync_playwright

def main():
    # Inicia Playwright
    with sync_playwright() as p:
        # Lanza el navegador (Chromium en este caso)
        browser = p.chromium.launch(headless=False)  # headless=False muestra el navegador
        page = browser.new_page()  # Crea una nueva pestaña
        
        # Navega a la URL deseada
        page.goto("https://example.com")
        
        # Espera unos segundos para observar el resultado (opcional)
        page.wait_for_timeout(5000)
        
        # Cierra el navegador
        browser.close()

if __name__ == "__main__":
    main()
