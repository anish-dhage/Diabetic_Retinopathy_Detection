## Detection of Diabetic Retinopathy

# Goals:

India is set to emerge as the diabetic capital of the world. Almost two-thirds of all Type 2 and Type 1 diabetics are expected to develop Diabetic Retinopathy (DR) over a period of time, making it the leading cause of new-onset blindness. The most opportune time for the treatment is before any loss of vision, since even advanced diabetic retinopathy can be present when a person has no vision complaints or problems.
Vision lost to DR is sometimes irreversible. Early detection, timely treatment and appropriate follow-up care can reduce the risk of blindness by 95%. 
Projection of new cases of DR in urban India.
A majority of people with DR are unaware of the seriousness of the condition and do not get timely check-ups. Since it lacks early symptoms, DR makes it difficult to detect the disease with enough time to reverse its impacts.
Our tentative goal is to counter these statistics and make a product that helps the doctor verify his diagnosis of a DR screening based on fundus images.

# Target Demographic:

Our product is targeted mainly towards medical professionals, who can use it to verify their diagnosis.
Since our model works off of fundus images of the patient, the professional should have the knowledge and skills for colour fundus photography, which could then be used by our product, to produce a diagnosis.
Fundus photography has an edge over the direct ophthalmoscope as the latter needs a greater skill to perform and allows only a limited view of the fundus at a time. Fundus photography also provides widefield fundus images. In addition, with direct ophthalmoscopy, there is no means of keeping a record.
Use of such a product would increase the reliability of the diagnosis.

# Overview and Use Cases:

Screening for DR and monitoring disease progression, especially in the early asymptomatic stages, is effective for preventing visual loss and reducing costs for health systems. Most screening programs use digital colour fundus cameras to acquire colour photographs of the retina. These photographs are then examined for the presence of lesions indicative of DR, including microaneurysms (MAs), haemorrhages (HEMs), exudates (EXs), and cotton wool spots (CWSs).
The application of automated image analysis to digital fundus images may reduce the workload and costs by minimizing the number of photographs that need to be manually graded.
To maximize the clinical utility of automated grading, an algorithm to detect and classify diabetic retinopathy is needed. We will be developing an automated system for classification of Diabetic Retinopathy.

# Classification will be done based on the stages given below:

 1.Healthy Retina   2.Mild Non Proliferative  3.Moderate NPR        4.Severe NPR          5.Proliferative Retinopathy

Each of these stages have the own unique identifiers which will help the system determine and successfully classify the image into one of these stages.

# Requirements:
# Functional Requirements:

Our model will first convert the colour retina images to grey scale to bring better contrast between various features of the image being processed. 
As a single input image is too large to be processed will look to convert the image into a feature vector. From the feature vector, a smaller subset of features will be selected for further processing. It will allow for processing using a reduced representation of the initial input.
The feature extraction will use low level, flexible techniques such as active contours, blob detection and so on.
For purpose of Data Augmentation, we propose to use a library that is built on top of Pytorch. It will allow our model to better recognise different angles of the same image as a single input, remove inconsistencies and also prevent overfitting.
For pupose of augmentation, we will use multiple transforms such as changes in angle, lighting, flipping about vertical axis and so.
To further improve accuracy, we will also employ test time augmentation. 
We will finalise the finer details of the project in due course as the project moves forward.

# Usability requirements:

Once our model attains commendable accuracy and gives satisfactory results, we will develop a desktop application for the same, which will be easy and intuitive to use for the Medical Professionals. The fundus images will serve as the input for the application.

# Other Requirements:

To help our model achieve a high accuracy, we need more fundus images. Moreover, the images needs to be validated by Medical Professionals to ensure that our model is being trained on reliable dataset.

# Constraints and Dependencies:

Our attempt to develop a system to help detect Diabetic Retinopathy shall be limited by both amount of data available as well as by the need of a variety of methods to solve this problem. This stems from the difficulty in formalizing difference in similarly coloured components. Also opacity is a major hurdle as well as unavailability of images of the entire retina as the disease can affect any region of the retina and is not confined to just one portion.

# Evaluation Plan:
(how final evaluation of product is done in binary, trinary, and ternary model, how accuracy is measured) 
Using Cross entropy loss metric.
