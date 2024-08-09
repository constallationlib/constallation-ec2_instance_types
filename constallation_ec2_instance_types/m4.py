from instance_type import InstanceType

m4_large = InstanceType(
    instance_family="m4",
    instance_size="large",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Xen",
    vcpus=2,
    architecture="x86_64",
    cores=2,
    valid_cores=[1, 2],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.4,
    memory_gb=8.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Moderate",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=2,
    ipv6_support=True
)

m4_xlarge = InstanceType(
    instance_family="m4",
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
    memory_gb=16.0,
    storage_gb=None,
    storage_type=None,
    network_performance="High",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=4,
    ipv6_support=True
)

m4_2xlarge = InstanceType(
    instance_family="m4",
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
    memory_gb=32.0,
    storage_gb=None,
    storage_type=None,
    network_performance="High",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=4,
    ipv6_support=True
)

m4_4xlarge = InstanceType(
    instance_family="m4",
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
    memory_gb=64.0,
    storage_gb=None,
    storage_type=None,
    network_performance="High",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=8,
    ipv6_support=True
)

m4_10xlarge = InstanceType(
    instance_family="m4",
    instance_size="10xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Xen",
    vcpus=40,
    architecture="x86_64",
    cores=40,
    valid_cores=[10, 20, 40],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.4,
    memory_gb=160.0,
    storage_gb=None,
    storage_type=None,
    network_performance="10 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=8,
    ipv6_support=True
)

m4_16xlarge = InstanceType(
    instance_family="m4",
    instance_size="16xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Xen",
    vcpus=64,
    architecture="x86_64",
    cores=64,
    valid_cores=[16, 32, 64],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.4,
    memory_gb=256.0,
    storage_gb=None,
    storage_type=None,
    network_performance="20 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=8,
    ipv6_support=True
)