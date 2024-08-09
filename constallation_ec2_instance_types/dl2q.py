from instance_type import InstanceType

dl2q_24xlarge = InstanceType(
    instance_family="dl2q",
    instance_size="24xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=192,
    architecture="x86_64",
    cores=96,
    valid_cores=[48, 96, 192],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=2.5,
    memory_gb=768.0,
    storage_gb=None,
    storage_type=None,
    network_performance="400 Gigabit",
    instance_storage_gb=None,
    gpu=True,
    gpu_count=8,
    gpu_memory_gb=640.0,
    eni=50,
    ipv6_support=True
)