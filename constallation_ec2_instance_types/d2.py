from instance_type import InstanceType

d2_xlarge = InstanceType(
    instance_family="d2",
    instance_size="xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Xen",
    vcpus=4,
    architecture="x86_64",
    cores=4,
    valid_cores=[2, 4],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.4,
    memory_gb=30.5,
    storage_gb=6000,
    storage_type="HDD",
    network_performance="Moderate",
    instance_storage_gb=6000,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

d2_2xlarge = InstanceType(
    instance_family="d2",
    instance_size="2xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Xen",
    vcpus=8,
    architecture="x86_64",
    cores=8,
    valid_cores=[2, 4, 8],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.4,
    memory_gb=61.0,
    storage_gb=12000,
    storage_type="HDD",
    network_performance="High",
    instance_storage_gb=12000,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

d2_4xlarge = InstanceType(
    instance_family="d2",
    instance_size="4xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Xen",
    vcpus=16,
    architecture="x86_64",
    cores=16,
    valid_cores=[4, 8, 16],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.4,
    memory_gb=122.0,
    storage_gb=24000,
    storage_type="HDD",
    network_performance="High",
    instance_storage_gb=24000,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

d2_8xlarge = InstanceType(
    instance_family="d2",
    instance_size="8xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Xen",
    vcpus=36,
    architecture="x86_64",
    cores=36,
    valid_cores=[9, 18, 36],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.4,
    memory_gb=244.0,
    storage_gb=48000,
    storage_type="HDD",
    network_performance="High",
    instance_storage_gb=48000,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)