# SubTitle-offset
Small python script to offset timecode in srt file in case it is not in-sync with audio

    SubTitle-offset
  
1.srt
------------------
1
00:00:09,600 --> 00:00:11,909
<i>♪ some text</i>

2
00:00:13,440 --> 00:00:16,512
<i>♪ More more more</i>

3
00:00:17,280 --> 00:00:19,475
<i>♪ All we do is wait</i>

4
00:00:21,120 --> 00:00:23,953
<i>♪ ok</i>

------------------
python srtOffset.py 1.srt 1.out.srt 3,333 
------------------
1.out.srt
------------------
1
00:00:12,933 --> 00:00:15,242
<i>♪ some text</i>

2
00:00:16,773 --> 00:00:19,845
<i>♪ More more more</i>

3
00:00:20,613 --> 00:00:22,808
<i>♪ All we do is wait</i>

4
00:00:24,453 --> 00:00:27,286
<i>♪ ok</i>


------------------
#negative offset
python srtOffset.py 1.srt 1.out.srt -3,333 
------------------
1
00:00:12,267 --> 00:00:14,576
<i>♪ some text</i>

2
00:00:16,107 --> 00:00:19,179
<i>♪ More more more</i>

3
00:00:19,947 --> 00:00:22,142
<i>♪ All we do is wait</i>

4
00:00:23,787 --> 00:00:26,620
<i>♪ ok</i>


