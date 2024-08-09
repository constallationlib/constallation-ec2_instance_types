from instance_type import InstanceType

hpc6id_32xlarge = InstanceType(
    instance_family="hpc6id",
    instance_size="32xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=128,
    architecture="x86_64",
    cores=128,
    valid_cores=[32, 64, 128],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=3.5,
    memory_gb=512.0,
    storage_gb=7500,
    storage_type="NVMe SSD",
    network_performance="200 Gigabit",
    instance_storage_gb=7500,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=30,
    ipv6_support=True
)