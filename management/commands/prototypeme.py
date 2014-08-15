from django.core.management.base import BaseCommand


def camelcaseme(text):
    return ''.join(x for x in text.title() if not x.isspace())


class Command(BaseCommand):
    help = "create a new prototype. This will create a django template, url config, and basic direct to template CBV"

    def handle(self, name, *args, **options):
        with open('../../raw/tpl/%s.jade' % (name), 'a') as f:
            f.write("""//-%s-\\\\""" % (name,))

        with open('prototyper/templates/prototyper/%s.html' % (name), 'a') as f:
            f.write('<!-- %s -->' % (name,))

        with open('prototyper/views.py', 'a') as f:
            view = """
class %s(TemplateView):
    template_name='prototyper/%s.html'

""" % (camelcaseme(name), name)

            f.write(view)

        f.close()

        with open('prototyper/urls.py', 'r+') as f:
            f.seek(-3, 2)
            f.write("""
    url(r'^%s/$', %s.as_view(), name='%s'),
)
""" % (name, camelcaseme(name), name)
)
        return 'Template %s created. /prototyper/%s/ to view ' % (name, name)
