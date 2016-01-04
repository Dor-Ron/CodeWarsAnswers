class HTMLGen:
    def p(self, content):
        return "<p>" + content + "</p>"
    def a(self, content):
        return "<a>" + content + "</a>"
    def b(self, content):
        return "<b>" + content + "</b>"
    def body(self, content):
        return "<body>" + content + "</body>"
    def div(self, c):
        return "<div>" + c + "</div>"
    def span(self, c):
        return "<span>" + c + "</span>"
    def title(self, c):
        return "<title>" + c + "</title>"
    def comment(self, c):
        return "<!--" + c + "-->"
