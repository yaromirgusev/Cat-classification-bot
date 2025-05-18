from PIL import Image
import torchvision.transforms as transforms
import torch

def predict_image(image_path, model, device):
    image = Image.open(image_path)
    transform = transforms.Compose([
        transforms.Resize((224, 224)),  
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  
    ])
    image_tensor = transform(image).unsqueeze(0)  
    
    image_tensor = image_tensor.to(device)

    with torch.no_grad():
        output = model(image_tensor)
        top1=-10000
        top2=-10000
        top3=-10000
        top1_i = 0
        top2_i = 0
        top3_i = 0
        for i, j in enumerate(output[0]):
            if j > top1:
                top1=j
                top1_i = i
            elif j > top2 and j < top1 :
                top2 = j
                top2_i = i
            elif j > top3 and j < top2:
                top3 = j
                top3_i = i

    return top1_i, top2_i, top3_i