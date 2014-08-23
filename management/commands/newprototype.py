from django.core.management.base import BaseCommand


def camelcaseme(text):
    return ''.join(x for x in text.title() if not x.isspace())


class Command(BaseCommand):
    help = "creates a new prototype. This will create a django template, url config, and basic direct to template CBV"

    def handle(self, name, context=None, *args, **options):
        with open('../../raw/tpl/%s.jade' % (name), 'a') as f:
            f.write("""//-%s-\\\\""" % (name,))

        with open('protoman/templates/protoman/%s.html' % (name), 'a') as f:
            f.write('<!-- %s -->' % (name,))

        with open('protoman/views.py', 'a') as f:
            view = """
class %s(TemplateView):
    template_name = 'protoman/%s.html'

    def get_context_data(*args, **kwargs):
        c = super(%s, self).get_context_data(*args, **kwargs)
        c.append(%s)
        return c
""" % (camelcaseme(name), name, camelcaseme(name), context)

            f.write(view)

        f.close()

        with open('protoman/urls.py', 'r+') as f:
            f.seek(-3, 2)
            f.write("""
    url(r'^%s/$', %s.as_view(), name='%s'),
)
""" % (name, camelcaseme(name), name)
)

        return 'Template %s created. /protoman/%s/ to view ' % (name, name)
