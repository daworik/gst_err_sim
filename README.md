# gst_err_sim
Попытки в перехват Caps.

батники загружают видео на udp в заданных форматах. после чего происходит попытка забрать видео
с udp и написать его формат (пока только caps) при суффиксе -v батник выводит информацию о проекте
выглядит это как мешанина, но нужную строчку с капсом найти можно ближе к концу.
![image](https://i.imgur.com/9BjCVyv.png)
# GetCaps.bat
Батник который в теории просто сливает информацию о потоке в консоль с помощью суффикса `-v`.
По факту он ничего не делает, протсо протаивая пока не запутится другой скрипт, использующий udp.
В таком случае при fakesink он просто выдаст ошибку переполнения буффера, при fakesink dump=1 начнет расписывать ячейки памяти.
выглядит это как мешанина, но нужную строчку с капсом найти можно ближе к концу.
как поставить фильтр на капс так и не нашел.
# catch.py
попытка в отображение капса через файл питона

Как забрать капс от элемента в пайплайне нашел:
```
pipeline = Gst.parse_launch("udpsrc address=230.230.230.230 ! fakesink")
sink = pipeline.get_by_name("fakesink0")
pad = sink.get_static_pad("sink")
caps = pad.get_current_caps()

```
Как выводить не нашел, `print(caps)` выдает None