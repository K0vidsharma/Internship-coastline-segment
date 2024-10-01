import cv2

vid_lis = [1, 4, 5, 6, 7, 8, 9, 11, 12]


def generate_images(vid_link, image_no_start):
    vid_cap = cv2.VideoCapture(vid_link)

    image_no = image_no_start
    count = 0
    while vid_cap.isOpened():
        success, image = vid_cap.read()
        if success:
            image = cv2.resize(image, (512, 512))
            # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image_loc = f"/Users/kovidsharma/Desktop/Drone Object Detection/seg_data_new/image{image_no}.png"
            cv2.imwrite(image_loc, image)
            count += 30
            vid_cap.set(1, count)
            image_no += 1
        else:
            vid_cap.release()
            break

        print('Read a new image: ', success)


vid_link_list = [f"/Users/kovidsharma/Downloads/{i}.mp4" for i in vid_lis]

generate_images(vid_link_list[8], 218)