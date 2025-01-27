from instance_type import InstanceType

vt1_3xlarge = InstanceType(
    instance_family="vt1",
    instance_size="3xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=12,
    architecture="x86_64",
    cores=12,
    valid_cores=[6, 12],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.5,
    memory_gb=48.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 25 Gigabit",
    instance_storage_gb=None,
    gpu=True,
    gpu_count=1,
    gpu_memory_gb=8.0,
    eni=3,
    ipv6_support=True
)

vt1_6xlarge = InstanceType(
    instance_family="vt1",
    instance_size="6xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=24,
    architecture="x86_64",
    cores=24,
    valid_cores=[12, 24],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.5,
    memory_gb=96.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 25 Gigabit",
    instance_storage_gb=None,
    gpu=True,
    gpu_count=2,
    gpu_memory_gb=16.0,
    eni=4,
    ipv6_support=True
)

vt1_24xlarge = InstanceType(
    instance_family="vt1",
    instance_size="24xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=96,
    architecture="x86_64",
    cores=96,
    valid_cores=[24, 48, 96],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.5,
    memory_gb=384.0,
    storage_gb=None,
    storage_type=None,
    network_performance="75 Gigabit",
    instance_storage_gb=None,
    gpu=True,
    gpu_count=8,
    gpu_memory_gb=64.0,
    eni=15,
    ipv6_support=True
)