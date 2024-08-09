from instance_type import InstanceType

c5_large = InstanceType(
    instance_family="c5",
    instance_size="large",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=2,
    architecture="x86_64",
    cores=2,
    valid_cores=[1, 2],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=3.0,
    memory_gb=4.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 10 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

c5_xlarge = InstanceType(
    instance_family="c5",
    instance_size="xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=4,
    architecture="x86_64",
    cores=4,
    valid_cores=[2, 4],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=3.0,
    memory_gb=8.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 10 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

c5_2xlarge = InstanceType(
    instance_family="c5",
    instance_size="2xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=8,
    architecture="x86_64",
    cores=8,
    valid_cores=[2, 4, 8],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=3.0,
    memory_gb=16.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 10 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=4,
    ipv6_support=True
)

c5_4xlarge = InstanceType(
    instance_family="c5",
    instance_size="4xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=16,
    architecture="x86_64",
    cores=16,
    valid_cores=[4, 8, 16],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=3.0,
    memory_gb=32.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 10 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=4,
    ipv6_support=True
)

c5_9xlarge = InstanceType(
    instance_family="c5",
    instance_size="9xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=36,
    architecture="x86_64",
    cores=36,
    valid_cores=[9, 18,