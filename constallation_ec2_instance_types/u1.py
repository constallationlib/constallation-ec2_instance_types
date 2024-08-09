from instance_type import InstanceType

u_1tb1 = InstanceType(
    instance_family="u-1",
    instance_size="tb1",
    free_tier_eligible=False,
    bare_metal=True,
    hypervisor=None,  # No hypervisor for bare metal instances
    vcpus=96,
    architecture="x86_64",
    cores=48,
    valid_cores=[12, 24, 48, 96],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=3.1,
    memory_gb=1024.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 25 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=15,
    ipv6_support=True
)

u_1tb1_24xlarge = InstanceType(
    instance_family="u-1",
    instance_size="24xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=96,
    architecture="x86_64",
    cores=48,
    valid_cores=[12, 24, 48, 96],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=3.1,
    memory_gb=1024.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 25 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=15,
    ipv6_support=True
)

u_1tb1_metal = InstanceType(
    instance_family="u-1",
    instance_size="metal",
    free_tier_eligible=False,
    bare_metal=True,
    hypervisor=None,  # No hypervisor for bare metal instances
    vcpus=96,
    architecture="x86_64",
    cores=48,
    valid_cores=[12, 24, 48, 96],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=3.1,
    memory_gb=1024.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 25 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=15,
    ipv6_support=True
)