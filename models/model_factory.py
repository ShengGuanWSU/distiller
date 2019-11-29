import models
import torch
model_dict = {
    "WRN10_4": models.wide.WRN10_4,  # params: 1198810
    "WRN16_1": models.wide.WRN16_1,  # params: 175066
    "WRN16_2": models.wide.WRN16_2,  # params: 691674
    "WRN16_4": models.wide.WRN16_4,  # params: 2748890
    "WRN16_8": models.wide.WRN16_8,  # params: 10961370
    "WRN28_2": models.wide.WRN28_2,  # params: 1467610
    "WRN22_4": models.wide.WRN22_4,  # params: 4298970
    "WRN22_8": models.wide.WRN22_8,  # params: 17158106
    "WRN28_1": models.wide.WRN28_1,  # params: 369498
    "WRN10_1": models.wide.WRN10_1,  # params: 77850
    "WRN40_1": models.wide.WRN40_1,  # params: 563930
    "WRN40_4": models.wide.WRN40_4,  # params: 8949210
    "resnet8_sm": models.cifar10sm.resnet8,  # params: 78042
    "resnet14_sm": models.cifar10sm.resnet14,  # params: 175258
    "resnet20_sm": models.cifar10sm.resnet20,  # params: 272474
    "resnet32_sm": models.cifar10sm.resnet32,  # params: 466906
    "resnet44_sm": models.cifar10sm.resnet44,  # params: 661338
    "resnet56_sm": models.cifar10sm.resnet56,  # params: 855770
    "resnet110_sm": models.cifar10sm.resnet110,  # params: 1730714
    "resnet1202_sm": models.cifar10sm.resnet1202,  # params: 19424026
    "resnet164_sm": models.cifar10sm.resnet164,  # params: 1704154
    "resnet1001_sm": models.cifar10sm.resnet1001,  # params: 10328602
    "resnet8": models.cifar10.resnet8,  # params: 89322
    "resnet10": models.cifar10.resnet10,  # params: 4903242
    "resnet18": models.cifar10.resnet18,  # params: 11173962
    "resnet34": models.cifar10.resnet34,  # params: 21282122
    "resnet50": models.cifar10.resnet50,  # params: 23520842
    "resnet101": models.cifar10.resnet101,  # params: 42512970
    "resnet152": models.cifar10.resnet152,  # params: 58156618
    "vgg11": models.cifar10.VGG11,  # params: 9231114
    "vgg13": models.cifar10.VGG13,  # params: 9416010
    "vgg16": models.cifar10.VGG16,  # params: 14728266
    "vgg19": models.cifar10.VGG19,  # params: 20040522
    "efficientnet": models.cifar10.EfficientNetB0,  # params: 2912089
}


def create_cnn_model(name, num_classes, device):
    print(f"Building model {name}...")
    model_cls = model_dict[name]
    model = model_cls(num_classes=num_classes)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"{name} total parameters: {total_params}")
    # always use dataparallel for now
    model = torch.nn.DataParallel(model)
    device_count = torch.cuda.device_count()
    print(f"Using {device_count} GPU(s).")
    # copy to cuda if activated
    model = model.to(device)
    return model


# for model in model_dict.keys():
#     create_cnn_model(model, 10, "cpu")
