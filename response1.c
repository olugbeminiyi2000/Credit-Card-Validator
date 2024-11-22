import re

class ArticleManager:
    def __init__(self, article_text, options=None):
        if not isinstance(article_text, str):
            raise ValueError("Article text must be a string.")
        if options is None:
            options = {}

        self.article_text = article_text
        self.pages = []
        self.words = []
        self.options = {
            'words_per_line': options.get('words_per_line', 12),
            'lines_per_page': options.get('lines_per_page', 20),
            'payment_structure': options.get('payment_structure', {
                1: 30,
                2: 30,
                3: 60,
                4: 60,
                'default': 100,
            })
        }

    def split_into_pages(self):
        words_per_line = self.options['words_per_line']
        lines_per_page = self.options['lines_per_page']
        words_per_page = words_per_line * lines_per_page

        # Split article text into words
        self.words = re.split(r'\s+', self.article_text.strip())

        # Split words into pages
        for i in range(0, len(self.words), words_per_page):
            page_words = self.words[i:i + words_per_page]
            page_lines = [' '.join(page_words[j:j + words_per_line]) 
                          for j in range(0, len(page_words), words_per_line)]
            self.pages.append('\n'.join(page_lines))

    def calculate_payment(self):
        words_per_page = self.options['words_per_line'] * self.options['lines_per_page']
        total_words = len(self.words)
        paid_pages = total_words // words_per_page  # Only count complete pages for payment

        if paid_pages < 1:
            return 0
        elif 1 <= paid_pages <= 2:
            return 30
        elif 3 <= paid_pages <= 4:
            return 60
        else:
            return 100

    def display_pages(self):
        for index, page in enumerate(self.pages):
            print(f"\nPage {index + 1}:\n{page}\n")

        total_pages = len(self.pages)
        payment = self.calculate_payment()
        print(f"Total Pages: {total_pages}")
        print(f"Payment Due: ${payment}")

    def process_article(self):
        self.split_into_pages()
        self.display_pages()

# Example Usage
article_text = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore "
    "et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea "
    "commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
    "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est "
    "laborum."
)

article_manager = ArticleManager(article_text)
article_manager.process_article()
