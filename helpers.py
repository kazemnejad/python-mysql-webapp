class HtmlRenderHelper:

    @staticmethod
    def render_main_page(jinjaEnv, **context):
        lefts = ["0", "323", "646"]
        tops = ["0", "588", "1176"]

        context["lefts"] = lefts
        context["tops"] = tops

        t = jinjaEnv.get_template("index.html")
        return t.render(context)
