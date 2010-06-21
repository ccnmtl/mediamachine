from django.core.management.base import BaseCommand, CommandError
from machine.models import Video, Resource, Theme, Keyword
import csv

class Command(BaseCommand):
    args = ''
    help = 'import dumps from csv'

    def handle(self, *args, **options):
        reader = csv.reader(open("dumps/MM_MEDIAMACHINE_T.csv"))
        video_ids_old_to_new = dict()
        for row in reader:
            (old_id,title,scene,author,copyrightholder,copyrightdate,
             created,modified,full_text,questions,commentary,plot,
             screenplay,image_url,real_video_url,sequence_url,
             local_video,real_video_filename,local_image,
             image_filename,sequence_prefix,sequence_count) = row
            # some quick conversions
            local_video = local_video == "YES"
            local_image = local_image == "YES"
            if copyrightdate == "":
                copyrightdate = 0
            if sequence_count == "":
                sequence_count = 0
            print old_id, title, author, copyrightdate, sequence_count
            v = Video.objects.create(title=title,scene=scene,
                                     author=unicode(author,errors='replace'),copyrightholder=unicode(copyrightholder,errors='replace'),
                                     copyrightdate=copyrightdate,
                                     created=created,modified=modified,
                                     full_text=full_text,questions=questions,
                                     commentary=commentary,plot=plot,
                                     screenplay=screenplay,image_url=image_url,
                                     real_video_url=real_video_url,
                                     sequence_url=sequence_url,
                                     local_video=local_video,
                                     real_video_filename=real_video_filename,
                                     local_image=local_image,
                                     image_filename=image_filename,
                                     sequence_prefix=sequence_prefix,
                                     sequence_count=sequence_count)
            video_ids_old_to_new[old_id] = v

        for row in csv.reader(open("dumps/MM_RESOURCE_T.csv")):
            (old_id,video_id,resource,description) = row
            video = video_ids_old_to_new[video_id]
            r,created = Resource.objects.get_or_create(resource=resource,description=description)
            video.resources.add(r)
            video.save()
        
        for row in csv.reader(open("dumps/MM_THEME_T.csv")):
            (old_id,video_id,theme) = row
            if video_id in video_ids_old_to_new:
                video = video_ids_old_to_new[video_id]
                t,created = Theme.objects.get_or_create(theme=theme)
                video.themes.add(t)
                video.save()

        for row in csv.reader(open("dumps/MM_KEYWORD_T.csv")):
            (old_id,video_id,keyword) = row
            if video_id in video_ids_old_to_new:
                video = video_ids_old_to_new[video_id]
                k,created = Keyword.objects.get_or_create(keyword=keyword)
                video.keywords.add(k)
                video.save()
                
