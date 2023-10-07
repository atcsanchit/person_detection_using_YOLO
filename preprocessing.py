import os
import cv2

def video_click(input_dir,output_dir,target_size=(224,224)):
    for files in os.listdir(input_dir):
        video_path=os.path.join(input_dir,files)
        cap = cv2.VideoCapture(video_path)

        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))

        for n in range(frame_count):
            ref,frame = cap.read()
            if ref:
                cv2.namedWindow("cctv footage",cv2.WINDOW_NORMAL)
                cv2.imshow("cctv footage",frame)
                cv2.resizeWindow("cctv footage",1000,500)
                cv2.waitKey(1)

            # resized_frame = cv2.resize(frame,target_size, fx=0.5, fy=0.5)
            output_filename = files + "_frame_" + str(n) + ".jpg"
            output_path = os.path.join(output_dir, output_filename)
            cv2.imwrite(output_path, frame)

            if cv2.waitKey(1) & 0xFF==ord("q"):
                break


        cap.release()


if __name__== "__main__":
    input_dir = os.path.join(".","open cv","video")
    output_dir = os.path.join(".","open cv","train_dataset")
    video_click(input_dir,output_dir)


