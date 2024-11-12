from bs4 import BeautifulSoup


def to_handle(response_text: list[str]):
    coffe_type = {}
    for text in response_text:
        soup = BeautifulSoup(text, "html.parser")
        coffe_name = soup.find("h1", class_="ty-mainbox-title").find("span").get_text(strip=True)
        ingredients_html = None
        try:
            ingredients_html = soup.find("ul", class_="marked").find_all("li")
        except AttributeError:
            pass
        if ingredients_html is None:
            ingredients_html = soup.find("div", class_="cmx-blog-page__content cmx-blog-page-content").find(
                "ul").find_all("li")
        ingredients = []
        for ingredient in ingredients_html:
            ingredient = ingredient.text.strip(";. ").split("–")
            if len(ingredient) == 1 and ":" in ingredient[0]:
                ingredient = ingredient[0].split(":")
            ingredients.append(ingredient)

        coffe_type[coffe_name] = ingredients
        print(coffe_type)
