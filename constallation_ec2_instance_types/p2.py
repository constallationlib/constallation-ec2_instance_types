from instance_type import InstanceType

p2_xlarge = InstanceType(
    instance_family="p2",
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
    sustained_clock_speed=2.7,
    memory_gb=61.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Moderate",
    instance_storage_gb=None,
    gpu=True,
    gpu_count=1,
    gpu_memory_gb=12.0,
    eni=2,
    ipv6_support=True
)

p2_8xlarge = InstanceType(
    instance_family="p2",
    instance_size="8xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Xen",
    vcpus=32,
    architecture="x86_64",
    cores=32,
    valid_cores=[8, 16, 32],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.7,
    memory_gb=488.0,
    storage_gb=None,
    storage_type=None,
    network_performance="High",
    instance_storage_gb=None,
    gpu=True,
    gpu_count=8,
    gpu_memory_gb=96.0,
    eni=4,
    ipv6_support=True
)

p2_16xlarge = InstanceType(
    instance_family="p2",
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
    sustained_clock_speed=2.7,
    memory_gb=732.0,
    storage_gb=None,
    storage_type=None,
    network_performance="20 Gigabit",
    instance_storage_gb=None,
    gpu=True,
    gpu_count=16,
    gpu_memory_gb=192.0,
    eni=8,
    ipv6_support=True
)